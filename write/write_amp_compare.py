"""
程式碼功能
1. 產生一個空 csv 檔案，使用 wb+ 以二進制寫方式打開，可以讀、寫文件， 如果文件不存在，創建該文件；如果文件已存在，先清空，再打開文件
2. 將需要做比較的兩個 csv 檔案分別取出子載波，計算其振幅和相位值之後，儲存到空的 csv 檔案
問題 : 輸出的 csv 檔案的第一列(column)會顯示單一數字，第二列(column)則是顯示正常
"""
import csv
import re
from math import sqrt, atan2
import pandas as pd

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """
    FILE_NAME0 = "C:/PythonProject/plot_csi_figure/src/old/write/compare1.csv"
    FILE_NAME1 = "C:/PythonProject/plot_csi_figure/src/old/1205/no-people/no-people-1.csv"
    FILE_NAME2 = "C:/PythonProject/plot_csi_figure/src/old/1205/people/people-1.csv"

    # f0 = open(FILE_NAME0, 'wb+')     # 清空 csv 檔案，參考 https://developer.aliyun.com/article/557213
    # with open(FILE_NAME0, 'w', newline='') as file:
        # writer = csv.writer(file)
        # writer.writerow(['沒人', '有人'])
    f1 = open(FILE_NAME1)
    f2 = open(FILE_NAME2)

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

        # 計算數據子載波的平均，分成上、下兩部分
        m1 = 0
        a1 = amplitudes1[6:32]      # len = 26
        # print('上半部子載波', a1)
        for a in a1:
            n = float(a)
            m1 += n
        mean1 = m1 / len(a1)
        # print('上半部的平均', format(mean1, '.3f'))
        m2 = 0
        a2 = amplitudes1[33:59]     # len = 26
        # print('下半部子載波', a2)
        for b in a2:
            n = float(b)
            m2 += n
        mean2 = m2 / len(a2)
        # print('下半部的平均', format(mean2, '.3f'))

        mean_no_people = format((mean1 + mean2) / 2, '.3f')
        # print(mean_no_people, file=open(FILE_NAME0, 'a'))
        # print("average#{}:".format(j1), mean_no_people, file=open('no_people_amp-0.csv', 'a'))
        with open(FILE_NAME0, 'a', newline='') as f0:
            writer = csv.writer(f0, delimiter=' ')
            writer.writerow(mean_no_people)

    for j2, l2 in enumerate(f2.readlines()):
        imaginary2 = []
        real2 = []
        amplitudes2 = []
        phases2 = []

        # Parse string to create integer list
        csi_string2 = re.findall(r"\[(.*)\]", l2)[0]
        csi_raw2 = [int(x) for x in csi_string2.split(" ") if x != '']

        # Create list of imaginary and real numbers from CSI
        for i in range(len(csi_raw2)):
            if i % 2 == 0:
                imaginary2.append(csi_raw2[i])
            else:
                real2.append(csi_raw2[i])

        # Transform imaginary and real into amplitude and phase
        for i in range(int(len(csi_raw2) / 2)):
            # 把計算後的振幅值取 3 位小數點後，放入 list 裡
            amplitudes2.append(format(sqrt(imaginary2[i] ** 2 + real2[i] ** 2), '.3f'))
            phases2.append(format(atan2(imaginary2[i], real2[i]), '.3f'))

        # 計算數據子載波的平均，分成上、下兩部分
        m3 = 0
        a3 = amplitudes2[6:32]      # len = 26
        # print('上半部子載波', a1)
        for x in a3:
            o = float(x)
            m3 += o
        mean3 = m3 / len(a3)
        # print('上半部的平均', format(mean1, '.3f'))
        m4 = 0
        a4 = amplitudes2[33:59]     # len = 26
        # print('下半部子載波', a2)
        for y in a4:
            p = float(y)
            m4 += p
        mean4 = m4 / len(a4)
        # print('下半部的平均', format(mean2, '.3f'))

        mean_people = format((mean3 + mean4) / 2, '.3f')
        # print("people_average#{}:".format(j2), mean_people)
        # print(mean_people, file=open(FILE_NAME0, 'a'))

        # list_mean = [mean_no_people, mean_people]
        # print(list_mean)
        # print(list_mean, file=open(FILE_NAME0, 'a'))
        # with open(FILE_NAME0, 'a', newline='') as file:
            # writer = csv.writer(file)
            # writer.writerow(list_mean)

    print("寫入完成!")
