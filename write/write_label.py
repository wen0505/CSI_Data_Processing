"""
程式碼功能:
能夠讀取一個 csv 檔案中特定行數的 csi data ，可以指定要顯示多少列，再儲存到空的檔案
"""
import csv

import pandas as pd

if __name__ == "__main__":
    """
    This script file demonstrates how to transform raw CSI out from the ESP32 into CSI-amplitude and CSI-phase.
    """

    FILE_NAME0 = "C:/PythonProject/plot_csi_figure/src/old/sit.csv"    # 空的 csv 檔案
    FILE_NAME1 = "C:/Users/lab517/Desktop/Android CSI/Data/站-坐/0223/backup1677148333149.csv"    # 原始 csv 檔案

    # f0 = open(FILE_NAME0, 'wb+')     # 清空 csv 檔案
    f1 = open(FILE_NAME1)

    loop1 = 1

    for j1, l1 in enumerate(f1.readlines()):
        if j1 >= 15724:     # 因為 j1 是從 0 開始計算，如果要讀取 20 行，需要將 j1 設為  19
            print(l1, end=' ', file=open(FILE_NAME0, 'a'))
            # print(l1)

            if loop1 >= 605:      # 會顯示 loop1 行
                break

            loop1 += 1

    print("寫入完成!")

    # df = pd.read_csv(FILE_NAME1, skiprows=10, nrows=3)
    # df.to_csv(FILE_NAME0)
