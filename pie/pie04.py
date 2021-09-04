import matplotlib.pyplot as plt

data = [244, 231, 103, 123]
lbl = ['A', 'B', 'AB', 'O']

plt.rc('font', family = 'D2Coding')
plt.axis('equal')
plt.pie(data, labels=lbl, autopct='%.1f%%')
plt.legend()
plt.show()