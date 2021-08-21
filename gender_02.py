import csv
import matplotlib.pyplot as plt

f = open('202107_gender.csv')
data = csv.reader(f)

header = next(data)

# 데이터 인덱스 추출
m_start_idx = header.index('2021년07월_남_0세')
m_end_idx = header.index('2021년07월_남_100세 이상')
f_start_idx = header.index('2021년07월_여_0세')

res_m = []
res_f = []
# 데이터 추출
for one in data:
    if '범계' in one[0]:
        res_m = one[m_start_idx:m_end_idx+1]
        res_f = one[f_start_idx:]

print(f'여 데이터 수: {len(res_f)}, 남 데이터 수 : {len(res_f)}')

res_m = list(map(int, res_m))
res_f = list(map(int, res_f))

# plt.plot(res_m, label='male')
# plt.plot(res_f, label='female')
plt.bar(range(101), res_m, label='male')
plt.bar(range(101), res_f, label='female')
plt.legend()
plt.show()