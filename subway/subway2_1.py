import csv

f = open("2021년_8월_유무임별.csv")
data = csv.reader(f)

header = next(data)
print(header)

# 데이터 샘플 출력
for i in range(5):
    one = next(data)
    print(one)

    # 데이터 가공하기 one[4]: 유임승차
    for i in range(4, 8):
        one[i] = int(one[i].replace(',', ''))

    print('가공후: ', one)
