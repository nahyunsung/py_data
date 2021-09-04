import csv

f = open('../pie/202107_gender.csv')
data = csv.reader(f)

header = next(data)
print(header)

print('남 데이터 시작점: ', header.index('2021년07월_남_0세'))
print('남 데이터 끝점: ', header.index('2021년07월_남_100세 이상'))
print('여 데이터 시작점: ', header.index('2021년07월_남_0세'))
print('여 데이터 끝점: ', header.index('2021년07월_남_100세 이상'))

res_m = header[3:104]
res_f = header[106:]
print(res_m)
print(res_f)

