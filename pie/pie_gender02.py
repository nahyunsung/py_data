import csv
import matplotlib.pyplot as plt

f = open('202107_gender.csv')
data = csv.reader(f)

# 필드명 추출
header = next(data)
print(header)

NUMBER = 101
m_cnt = 0
f_cnt = 0

m_idx = header.index("2021년07월_남_0세")
f_idx = header.index("2021년07월_여_0세")

area = '범계'

# 지역별 성별 나이 구간의 합 구하기
for one in data:
    tmp_area = one[0]
    if area in tmp_area:
        for idx in range(NUMBER):
            m_cnt += int(one[m_idx].replace(',',''))
            f_cnt += int(one[f_idx].replace(',',''))
        break

lbl = ["남", "여"]
plt.rc('font', family = "D2Coding")
plt.title(f'{area}지역의 남여 성별 인구')
plt.pie([m_cnt, f_cnt], autopct="%.1f%%", labels=lbl, startangle=90)
plt.legend(loc=8)
plt.show()