import csv
import matplotlib.pyplot as plt


f = open("../pie/202107_gender.csv")
data = csv.reader(f)

header = next(data)
# print(header)

# 자료 시작 인덱 추출
# 0~100세 총 101구간
NUM = 101
m_idx = header.index("2021년07월_남_0세")
f_idx = header.index("2021년07월_여_0세")
# print(f"남자 인구수 시작: {m_idx}, 여자 인구수 시작: {f_idx}")

# 지역설정
area = "범계"

# 지역별 인구 수 추출
m_lst = []
f_lst = []

for one in data:
    tmp_area = one[0]
    if area in tmp_area:
        # 해당 데이터의 나이별 남, 여 인구수 리스트에 저장
        m_lst = one[m_idx:m_idx+NUM]
        f_lst = one[f_idx:f_idx+NUM]

# print("지역별 성별 연령대 인구수: (남)", m_lst)
# print("지역별 성별 연령대 인구수: (여)", f_lst)

# 성별 인구수 리스트 형변화(문자-> 정수)
m_lst = list(map(int, m_lst))
f_lst = list(map(int, f_lst))

print("지역별 성별 연령대 인구수: (남)", m_lst)
print("지역별 성별 연령대 인구수: (여)", f_lst)

# 항아리 모양 그래프 그리기
for idx, one in enumerate(f_lst):
    f_lst[idx] = one * -1
print("지역별 성별 연령대 인구수: (여)", f_lst)

# 그래프 그리기
plt.barh(range(101), m_lst)
plt.barh(range(101), f_lst)
plt.show()