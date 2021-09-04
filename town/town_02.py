import csv
import matplotlib.pyplot as plt

f = open('../202107_age.csv')
data = csv.reader(f)

# 필드명 추출
header = next(data)

result = []
for one in data:
    if '안양시' in one[0]:
        result = one[3:]
        break

# 데이터 처리
result = [one.replace(',','') for one in result]
result = list(map(int, result))
print(result)

plt.style.use('ggplot')
plt.rc('font', family='D2Coding')
plt.title('안양시 나이별 인구수')
plt.plot(result)
plt.show()