"""
參考網站 : https://blog.csdn.net/weixin_48135624/article/details/113939429
程式碼功能 : 能將資料夾內所有的 csv 檔案合併成一個 csv 檔案
"""
from glob import glob

csv_list = glob.glob('.\\merge\\*.csv')
print("共發現", len(csv_list), "個 CSV 檔案")
for i in csv_list:
    fr = open(i, 'rb').read()
    with open('combined.csv', 'ab') as f:
        f.write(fr)
print('合併完成')
