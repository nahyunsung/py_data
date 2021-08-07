# 기온 최대값 구하기

import csv

# 파일 불러오기
file = open('seoul_1904.csv', 'r')
data = csv.reader(file)

# 불필요한 행 데이터 넘기기
for i in range(7):
    next(data)

# 필드명 저장
header = next(data)

tmp_max = -99999
max_data = ''
for one in data:
    if one:
        if one[-1] != '':
            smax_temp = float(one[-1])
            if smax_temp > tmp_max:
                tmp_max = smax_temp
                max_data = one[0]

print(tmp_max, max_data)