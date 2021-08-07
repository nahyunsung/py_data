#  서울 기온 불러오기

import csv

# open(파일이름, 모드(읽기), 인코딩)
# csv.reader(파일, 구분자)
file = open('seoul_1904.csv', 'r', encoding='cp949')
data = csv.reader(file, delimiter=',')
print(data)

# 데이터 출력
for idx, one in enumerate(data):
    if idx > 20: break
    print(one)


file.close()