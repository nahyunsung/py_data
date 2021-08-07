# 서울 기온 불러오기
# 불필요한 행 정리하기

import csv

file = open('seoul_1904.csv', 'r')
data = csv.reader(file)

# 불필요한 행 넘기기
for i in range(7):
    next(data)

headers = next(data)
print('필드명: ', headers)

for idx, one in enumerate(data):
    print(one)
    if idx > 20: break

file.close()