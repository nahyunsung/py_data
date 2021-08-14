import csv
import matplotlib.pyplot as plt

f = open('seoul_1904_2.csv.csv')
data = csv.reader(f)

# 필드명 리스트 추출
header = next(data)

b_month = 1
b_day = 20
# 생일 최고 기온 리스트 초기화
b_temp = []

# 데이터 값 추출
for one in data:
    date = one[0]
    date = date.split('-')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    # 추출 데이터의 날짜가 생일과 동일하면 추가
    if year >= 1980:
        if b_month == month and b_day == day:
            if one[-1] != '':
                tmp = float(one[-1])
                b_temp.append(tmp)

# 리스트 값 출력
print(b_temp)

# 수집 자료 개수
print(len(b_temp))

plt.plot(b_temp)
plt.show()