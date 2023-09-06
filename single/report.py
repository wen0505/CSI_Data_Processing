# 單張圖片
import re
from math import sqrt, atan2

from matplotlib import pyplot as plt

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """

    FILE_NAME1 = "C:/PythonProject/plot_csi_figure/src/old/csv_raw/sit.csv"

    f1 = open(FILE_NAME1)

    j0 = 3156

    loop = 1                   # 設定總共要顯示多少個子圖
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

            plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']    # 用來正常顯示中文標籤
            plt.rcParams['axes.unicode_minus'] = False                  # 用來正常顯示負號
            # plt.title('室內的狀態', fontsize=20)
            # plt.xlabel('子載波數 (單位:個)', fontsize=15)
            # plt.ylabel('振幅 (單位:dB)', fontsize=15)
            plt.xlim(0, 50)
            plt.ylim(0, 45)
            plt.plot(amplitudes1[5:60], 'r', linewidth=1, label='stand-left')
            plt.legend(loc='best')
            plt.show(block=True)

            loop1 += 1



