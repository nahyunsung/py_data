# 최다 승차승객수

import csv

f = open("2021년_8월_bus.csv")
data = csv.reader(f)

header = next(data)
print(header)

max_val = 0
max_data = ''

min_val = 1874711
min_data = ''

for one in data:
    # 승차승객수 정수로 변환
    num = int(one[4].replace(',',''))
    if num > max_val:
        max_val = num
        max_data = one
    if num < min_val:
        min_val = num
        min_data = one

max_sta = f'{max_data[3]} {max_data[1]}'
max_val = max_data[4]
min_sta = f'{min_data[3]} {min_data[1]}'
min_val = min_data[4]


print(f'최대승차정보: {max_sta} {max_val}명, {max_data[5]}')
print(f'최하승차정보: {min_sta} {min_val}명, {min_data[5]}')
