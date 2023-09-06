
filename = "dataset2.csv"
# test
n_start = 0
n_end = 3000

# 開啟檔案
with open(filename, 'w') as f:
    # 使用 for 迴圈逐一寫入資料
    for i in range(n_start, n_end):
        f.write("train2/walk-" + str(i) + ".png" + '\n')
    for i in range(n_start, n_end):
        f.write("train2/stand-" + str(i) + ".png" + '\n')
    for i in range(n_start, n_end):
        f.write("train2/sit-" + str(i) + ".png" + '\n')
    for i in range(n_start, n_end):
        f.write("train2/squat-" + str(i) + ".png" + '\n')

print("寫入完成")
