# 막대그래프
import matplotlib.pyplot as plt

data = [30, 50, 76, 40]
lbl_x = ['1학년', '2학년', '3학년', '4학년']

plt.rc('font', family='D2Coding')
plt.title('세로막대 그래프')
# plt.bar(range(len(data)), data)
plt.bar(lbl_x, data)
plt.show()