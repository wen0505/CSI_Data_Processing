"""
程式碼功能
1. 產生兩個空 csv 檔案，使用 wb+ 以二進制寫方式打開，可以讀、寫文件， 如果文件不存在，創建該文件；如果文件已存在，先清空，再打開文件
2. 將一個原始的 csv 檔案取出子載波，計算其振幅和相位值後，再計算其平均值和標準差，然後分別儲存到兩個空的 csv 檔案
"""
import re
from math import sqrt, atan2

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """
    FILE_NAME1 = "C:/PythonProject/plot_csi_figure/src/old/write/combined_people.csv"       # 原始 csv 檔案
    FILE_NAME2 = "C:/PythonProject/plot_csi_figure/src/old/write/people_phase-ave.csv"        # 新增加的平均值檔案
    FILE_NAME3 = "C:/PythonProject/plot_csi_figure/src/old/write/people_phase-sd.csv"         # 新增加的標準差檔案

    f1 = open(FILE_NAME1)
    f2 = open(FILE_NAME2, 'wb+')     # 清空 csv 檔案，參考 https://developer.aliyun.com/article/557213
    print('ave', file=open(FILE_NAME2, 'a'))
    f3 = open(FILE_NAME3, 'wb+')
    print('sd', file=open(FILE_NAME3, 'a'))

    loop1 = 0
    loop = 500      # 可以選擇要輸入幾行的資料

    for j1, l1 in enumerate(f1.readlines()):
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
            # 把計算後的振幅值取 3 位小數點後，放入 list 裡
            amplitudes1.append(format(sqrt(imaginary1[i] ** 2 + real1[i] ** 2), '.3f'))
            phases1.append(format(atan2(imaginary1[i], real1[i]), '.3f'))

        if loop1 >= loop:
            break

        # 將數據子載波的上、下兩部分整合成一個 list
        data_sub_amp = [element for e in [amplitudes1[6:32], amplitudes1[33:59]] for element in e]
        data_sub_phase = [element for e in [phases1[6:32], phases1[33:59]] for element in e]

        # 計算新 list 的平均值
        m = 0
        for a in data_sub_phase:
            n = float(a)
            m += n
        mean = m / len(data_sub_phase)
        # print('平均值 : ', format(mean, '.3f'))
        print(format(mean, '.3f'), file=open(FILE_NAME2, 'a'))

        # 計算新 list 的標準差，參考 : https://savingking.com.tw/blog/post/mean
        s = 0
        for d in data_sub_phase:
            b = float(d)
            s = s + (b - mean)**2
        sd = sqrt((s/(len(data_sub_phase)-1)))
        # print("標準差 : ", format(sd, '.3f'))
        print(format(sd, '.3f'), file=open(FILE_NAME3, 'a'))

        loop1 += 1

    print("寫入完成!")
