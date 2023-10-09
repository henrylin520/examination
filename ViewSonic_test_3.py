# -*- coding: utf-8 -*-
"""
ViewSonic examine
"""
import numpy as np
import csv

read_filename = 'data.txt'
write_filename = 'UserInformation.csv'

csv_title=['姓', '名', '身分證']

"""
1. 開啟txt檔案
2. 調整資料內容儲存成二維陣列
"""
fp = open(read_filename, 'r')
raw_content_txt = fp.readlines()
temp_list = []
last_name = ''
first_name = ''
i = 0

for line in raw_content_txt:
    temp = raw_content_txt[i].split(',')
    last_name = temp[0].split(' ')[1]
    temp_list.append(last_name)
    #print(temp_list)
    first_name = temp[0].split(' ')[0]
    temp_list.append(first_name)
    temp_list.append(temp[1])
    i += 1
 
two_array = np.array(temp_list).reshape(int(len(temp_list)/3), 3)
print(two_array)
fp.close() 

"""
1. 資料寫入csv檔
"""
with open(write_filename, 'w+', newline='') as fp_csv:
    writer = csv.writer(fp_csv)
    writer.writerow(csv_title)
    for row in two_array:
        writer.writerow(row)
fp_csv.close()

