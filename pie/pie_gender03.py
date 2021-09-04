import csv
import matplotlib.pyplot as plt

f = open("202107_gender.csv")
data = csv.reader(f)

header = next(data)
print(header)

m_sum_idx = header.index("2021년07월_남_연령구간인구수")
f_sum_idx = header.index("2021년07월_여_연령구간인구수")

area = "범계"
m_sum = 0
f_sum = 0

for one in data:
    if area in one[0]:
        m_sum = int(one[m_sum_idx].replace(',', ''))
        f_sum = int(one[f_sum_idx].replace(',', ''))
        break

print(m_sum)
print(f_sum)

lbl = (["남", "여"])
plt.rc('font', family="D2Coding")
plt.pie([m_sum, f_sum], labels=lbl)
plt.show()