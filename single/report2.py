"""
程式碼功能:
能夠讀取一個檔案特定單一列的 csi data ，可以指定要從哪一行開始讀取並控制需要顯示的列數，並計算子載波的振幅和相位值，並呈現在圖片上
P.S. 讀取檔案特定列參考 : https://www.twblogs.net/a/5f0342d25352062f754ebd21
"""
import re
from math import sqrt, atan2

from matplotlib import pyplot as plt

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """

    FILE_NAME1 = "C:/PythonProject/plot_csi_figure/src/old/csv_raw/sit.csv"

    f1 = open(FILE_NAME1)

    j0 = 3400                      # 要讀取第 n 行需要設定為 j0 == n-1

    loop = 100                  # 設定總共要顯示多少個子圖
    loop0 = int(sqrt(loop))     # 設定子圖為 loop0 * loop0 的形式
    loop1 = 0

    for j1, l1 in enumerate(f1.readlines()):
        if j1 >= j0:
            imaginary1 = []
            real1 = []
            amplitudes1 = []
            phases1 = []

            # Parse string to create integer list
            csi_string1 = re.findall(r"\[(.*)\]", l1)[0]
            csi_raw1 = [int(x) for x in csi_string1.split(" ") if x != '']

            # Create list of imaginary and real numbers from CSI
            for i in range(len(csi_raw1)):
                if i % 2 == 0:
                    imaginary1.append(csi_raw1[i])
                else:
                    real1.append(csi_raw1[i])

            # Transform imaginary and real into amplitude and phase
            for i in range(int(len(csi_raw1) / 2)):
                amplitudes1.append(sqrt(imaginary1[i] ** 2 + real1[i] ** 2))
                phases1.append(atan2(imaginary1[i], real1[i]))

            if loop1 >= loop:
                break

            plt.subplot(loop0, loop0, loop1+1)
            plt.title("frame"+str(loop1), fontsize=8)
            plt.xlim(0, 50)
            plt.ylim(0, 40)
            plt.xticks(fontsize=6)      # 設定座標軸刻度的文字大小
            plt.yticks(fontsize=6)
            plt.plot(amplitudes1[5:60], 'r', linewidth=0.6)

            loop1 += 1

    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']    # 用來正常顯示中文標籤
    plt.rcParams['axes.unicode_minus'] = False                  # 用來正常顯示負號
    plt.suptitle('室內的狀態', fontsize=20)
    # plt.title('目前的動作', fontsize=20)
    # plt.text(-290, -25, '子載波數 (單位:個)', fontsize=16, va='center')
    # plt.text(-570, 235, '振幅 (單位:dB)', fontsize=16, va='center', rotation='vertical')
    plt.legend(loc='best')

# plt.savefig("C:/Users/lab517/Desktop/Android CSI/Data/站-坐/stand/compare/stand_compare_81.PNG")
plt.show(block=True)
print("儲存圖片")
