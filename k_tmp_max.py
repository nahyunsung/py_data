# 경기(수원) 지역의 최고온도 구하기
# gg_1904.csv

import csv

file = open('gg_1904.csv', 'r')
data = csv.reader(file)
data = list(data)

data = data[8:-1]

max_tmp = 0
max_data = ''
for one in data:
    tmp = one[-1]
    if tmp == '':
        stmp = -9999
    else:
        stmp = float(one[-1])
    if stmp > max_tmp:
        max_tmp = stmp
        max_data = one[0]
print(max_tmp, max_data)