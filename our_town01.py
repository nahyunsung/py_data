import csv
import matplotlib.pyplot as plt

f = open('202107_n.csv.csv')
data = csv.reader(f)

header = next(data)
usr = '내손1동'

# one = next(data)
# print(one)
# print(one[0])

for one in data:
    if usr in one[0]:
        r_data = one[3:]
        # r_data = []
        # for x in one[3:]:
            # r_data.append(int(x))

# 데이터 확인
print(r_data)

r = list(map(int, r_data))

plt.plot(r)
plt.show()