"""
程式碼說明:
由於本研究是使用 YOLOv5 進行訓練，需要將一整張圖片標記成一個類別，但因為資料集裡的圖片數量眾多，所以將各類別標記一張圖片後，會產生各類別的 txt 標記檔。
使用此程式碼即可大量複製出每個類別的 txt 標記檔案。
"""
import shutil
import os

# 指定原始txt檔案的路徑
src_file = "C:/Users/lab517/PycharmProjects/datasets/action_gray/indoor/labels/train/walk-0.txt"

# 指定要複製到的目錄
dest_dir = "C:/Users/lab517/PycharmProjects/datasets/action_gray/indoor/labels/train/"

# 指定要複製的檔案副本數量
num_copies = 2999

# 遍歷檔案副本數量，將txt檔案複製到每個副本中
for i in range(num_copies):
    # 構造目標txt檔案的路徑
    dest_file = os.path.join(dest_dir, f"walk-{i+1}.txt")

    # 複製txt檔案到目標目錄
    shutil.copy(src_file, dest_file)

print("複製完成")
