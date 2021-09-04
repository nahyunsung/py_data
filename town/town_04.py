import csv
import matplotlib.pyplot as plt

f = open('../202107_age.csv')
data = csv.reader(f)

header = next(data)

town = input("인구수를 조회할 지역명(읍, 면, 동 단위)를 입력하세요 : ")

result = []
for one in data:
    if town in one[0]:
        result = one[3:]
        name = one[0]
        break

# print(name)
l = name.index(' (')
name = name[:l]


result = [one.replace(',','') for one in result]
result = list(map(int, result))

plt.style.use('ggplot')
plt.rc('font', family='D2Coding')
plt.title(name+" 나이별 인구 그래프")
plt.plot(result)
plt.show()