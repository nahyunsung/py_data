# 서울 기온 불러오기

import csv

file = open('seoul_1904.csv', 'r')
data = csv.reader(file)

for idx, one in enumerate(data):
    print(idx, one)
    if idx > 20: break

file.close()