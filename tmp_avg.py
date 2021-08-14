# 1004sus 이후 8월 1일의 평균 기온 그래프 그리기

import csv
import matplotlib.pyplot as plt

f = open('seoul_1904_2.csv.csv')
data = csv.reader(f)

hearder = next(data)
print(hearder)

s_month = 8
s_day = 1

# 1월 8월 평균 온도 데이터
avg_1tmp = []
avg_8tmp = []

for one in data:
    date = one[0]
    date = date.split('-')
    if int(date[1]) == s_month:
        if one[-3] != '':
            tmp = float(one[-3])
            avg_8tmp.append(tmp)
    if int(date[1]) == 1:
        if one[-3] != '':
            tmp = float(one[-3])
            avg_1tmp.append(tmp)

plt.hist(avg_1tmp, bins=100,  label = 'avg_1tmp', color='blue')
plt.hist(avg_8tmp, bins=100,  label = 'avg_8tmp', color='red')
plt.legend(loc='best')
plt.show()