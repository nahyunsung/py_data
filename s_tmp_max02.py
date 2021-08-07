import csv

file = open('seoul_1904.csv', 'r')
data = csv.reader(file)
data = list(data)

data = data[8:-1]

max_tmp = 0
max_data = ''

for one in data:
    tmp = one[-1]
    if tmp == '':
        s_tmp = -999
    else:
        s_tmp = float(one[-1])

    if s_tmp > max_tmp:
        max_tmp = s_tmp
        max_data = one[0]

print(f'1904년 이후 서울의 최고 기온은 {max_data}, {max_tmp}도 입니다')