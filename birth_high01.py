import csv
import matplotlib.pyplot as plt

f = open('seoul_1904_2.csv.csv')
data = csv.reader(f)

header = next(data)
print(header)

# 1행 데이터 추출
data1=next(data)
print(data1)

# 1행 데이터에서 날짜 추출
data = data1[0]
year = data[:4]
month = data[5:7]
day = data[8:]
print(data, year, month, day)

# 날짜 추출2
date = data1[0]
date = date.split('-')
print(date)
print(date[0], date[1]=='10', date[2])