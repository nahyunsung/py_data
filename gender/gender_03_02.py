import csv
import matplotlib.pyplot as plt

# 데이터 처리 함수 구현
def make_data(tmp_lst, sign = 1):
    # 성별 인구수 리스트 ',' 제거
    tmp_lst = [one.replace(',', '') for one in tmp_lst]

    tmp_lst = list(map(int, tmp_lst))

    # for idx, one in enumerate(f_lst):
    #     f_lst[idx] = one * -1

    tmp_lst = [one * sign for one in tmp_lst]
    return tmp_lst


f = open("../pie/202107_gender.csv")
data = csv.reader(f)

header = next(data)
# print(header)

m_idx = header.index("2021년07월_남_0세")
f_idx = header.index("2021년07월_여_0세")
# print(m_idx, f_idx)

m_lst = []
f_lst = []

area = "안양"

for one in data:
    if area in one[0]:
        m_lst = one[m_idx:m_idx+101]
        f_lst = one[f_idx:f_idx+101]
        break

# print(m_lst)
# print(f_lst)

# 데이터 처리 함수 호출
m_lst = make_data(m_lst)
f_lst = make_data(f_lst, -1)

plt.rc("font", family = 'D2Coding')
plt.title(f'{area}동 남여 인구 분포')
plt.barh(range(101), m_lst)
plt.barh(range(101), f_lst)
plt.show()