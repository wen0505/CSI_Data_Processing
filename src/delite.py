"""
程式碼功能:
可以將 CSV 檔案中缺失的部分刪除，然後儲存成新的檔案
"""
import pandas as pd
import csv

if __name__ == "__main__":

    FILE_NAME1 = "C:/PythonProject/plot_csi_figure/src/old/csv_raw/unmanned_old.csv"

    f1 = open(FILE_NAME1)

    loop1 = 1

    for j1, l1 in enumerate(f1.readlines()):
        if l1 == ']':
            print(j1)

    # data = pd.read_csv(FILE_NAME1, delimiter='\t')
    # new_data = data.dropna(axis=0, how='any')       # 直接刪除含有缺失值的行
    # new_data = data[data["CSI_DATA"].isnull()]
    # print(new_data)

    # print("Old data frame length:", len(data))
    # print("New data frame length:", len(new_data))
    # print("Number of rows with at least 1 NA value: ", (len(data)-len(new_data)))

    # 儲存成新的 csv 檔案
    # new_data.to_csv('./unmanned_new.csv', index=0)
