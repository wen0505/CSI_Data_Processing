"""
程式碼功能
1. 產生一個空 csv 檔案，使用 wb+ 以二進制寫方式打開，可以讀、寫文件， 如果文件不存在，創建該文件；如果文件已存在，先清空，再打開文件
2. 將單一一個 csv 檔案取出子載波，計算其振幅和相位值之後，儲存到空的 csv 檔案
"""
import csv
import re
from math import sqrt, atan2

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """
    FILE_NAME0 = "C:/PythonProject/plot_csi_figure/src/old/stand_amp.csv"       # 空的 csv 檔案
    FILE_NAME1 = "C:/PythonProject/plot_csi_figure/src/old/stand.csv"           # 原始 csv 檔案

    f0 = open(FILE_NAME0, 'wb+')     # 清空 csv 檔案
    index = list(range(1, 65))
    for i in index:
        print("index#{}:".format(i), end='\t', file=open(FILE_NAME0, 'a'))
    print('\n', file=open(FILE_NAME0, 'a'))
    f1 = open(FILE_NAME1)

    loop1 = 0
    loop_n = 3500                           # 設定總共要輸出多少筆資料

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

        if loop1 >= loop_n:
            break

        # 將數據子載波的上、下兩部分整合成一個 list
        data_sub = [element for e in [amplitudes1[6:32], amplitudes1[33:59]] for element in e]
        data_sub.extend(0 for _ in range(abs(64-len(data_sub))))

        # 把 list 寫入 csv 檔案
        with open(FILE_NAME0, 'a', newline='') as file:
            writer = csv.writer(file, delimiter='\t')
            writer.writerow(data_sub)

        loop1 += 1

    print("寫入完成!")
