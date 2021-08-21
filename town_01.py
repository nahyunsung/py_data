import csv

# 데이터 불러오기
f = open('202107_age.csv')
data = csv.reader(f)

# 필드명 추출
header = next(data)

# print(len(header), header)

# 우리 동네 인구수 기록
result = []

# 데이터 추출하기
for one in data:
    if '안양시' in one[0]:
        result = one[3:]
        break

for idx, num in enumerate(result):
    result[idx] = int(num.replace(',',''))

# 추출 데이터 보기
print(result)

for idx, cnt in enumerate(result):
    print(cnt)
    # print(f'{idx}세: {cnt}명')