import csv
import matplotlib.pyplot as plt

f = open('../202107_age.csv')
data = csv.reader(f)

header = next(data)

result = []
for one in data:
    if '범계동' in one[0]:
        result = one[3:]

result = list(map(int, result))

plt.style.use('ggplot')
plt.rc('font', family='D2Coding')
plt.title('범계동 나이별 인구수')
plt.plot(result)
plt.show()