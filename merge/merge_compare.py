import csv
import glob
import pandas as pd
from glob import glob

no_people_1 = pd.read_csv('.\\merge\\people_amp-n.csv')
people_1 = pd.read_csv('.\\merge\\people_amp-p.csv')
# merge_df = pd.concat([no_people_1, people_1])
merge_df = [no_people_1, people_1]
# print(merge_df)

# print(merge_df, file=open('compare_indoor.csv', 'a'))

# merge_df.to_csv('compare_indoor.csv', index=True, encoding='utf-8-sig')

with open('compare_indoor.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(merge_df)

print("寫入完成!")
