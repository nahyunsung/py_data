# 1980년이후 생일에 최고 최저 기온
import csv
import matplotlib.pyplot as plt

f = open('seoul_1904_2.csv.csv')
data = csv.reader(f)

# 필드명 추출
header = next(data)

# 변수 초기ㅗ하
b_month = 1
b_day = 20
b_temp_high = []
b_temp_low = []

# 데이터 추출하기
for one in data:
    # 날짜 추출
    date = one[0]
    date = date.split('-')
    year = int(date[0])
    if year >= 1980:
        month = int(date[1])
        day = int(date[2])
        if b_month == month and b_day == day:
            if one[-1] != '' and one[-2] != '':
                tmp_high = float(one[-1])
                tmp_low = float(one[-2])
                b_temp_high.append(tmp_high)
                b_temp_low.append(tmp_low)

plt.title('birth_tmp')
plt.plot(b_temp_low, label='low', color='blue')
plt.plot(b_temp_high, label='high', color='red')
plt.legend(loc='best')
plt.show()