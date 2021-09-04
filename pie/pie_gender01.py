import csv
import matplotlib.pyplot as plt

def cnt_list(tmp_lst):
    # 데이터 정리
    tmp_lst = [one.replace(',', '') for one in tmp_lst]

    tmp_lst = list(map(int, tmp_lst))

    print(f'{tmp_area}남 데이터: ', tmp_lst)

    return sum(tmp_lst)

f = open('202107_gender.csv')
data = csv.reader(f)

header = next(data)
print(header)

m_idx = header.index("2021년07월_남_0세")
f_idx = header.index("2021년07월_여_0세")
print(f"남자 데이터 시작 인덱스: {m_idx}번째 데이터")
print(f"여 데이터 시작 인덱스: {f_idx}번째 데이터")

# 지역 설정
area = '안양'
NUM = 101

# 지역별 성별 인구수 추출
for one in data:
    tmp_area = one[0]
    if area in tmp_area:
        result_m = one[m_idx:m_idx+NUM]
        result_f = one[f_idx:f_idx+NUM]
        break
print(f'{tmp_area}남 데이터: ', result_m)
print(f'{tmp_area}남 데이터: ', result_f)

# 성별 총 인구수 구하기
# cnt_list(인수: list) > 반환값: list dnjstndml 합

num_m = cnt_list(result_m)
num_f = cnt_list(result_f)
print(f'{tmp_area}지역 남자 총 {num_m}명')
print(f'{tmp_area}지역 여자 총 {num_m}명')

pie_data = [num_m, num_f]
pie_lbl = [f'남({num_m}명)', f'여({num_f}명)']
color = ["blue", "red"]

plt.rc('font', family='D2Coding')
plt.title(f'{area}지역 성별 인구수')
plt.pie(pie_data, labels=pie_lbl, colors=color, autopct="%.1f%%", startangle=90)
plt.legend()
plt.show()