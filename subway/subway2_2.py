import csv

f = open("2021년_8월_유무임별.csv")
data = csv.reader(f)

header = next(data)
print(header)


# 3. 데이터 추출
for one in data:
    # 수치 데이터 정수 변환
    for i in range(4, 8):
        one[i] = one[i].replace(',','') # , 제거
        one[i] = int(one[i])            # 정수변환
    if one[6] != 0:
        rate = one[4] / (one[4] + one[6])
        print(one, rate)