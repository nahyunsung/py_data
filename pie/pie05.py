import matplotlib.pyplot as plt

data = [244, 231, 103, 123]
lbl = ['A', 'B', 'AB', 'O']
color = ["darkmagenta", "pink", "skyblue", "hotpink"]

plt.rc('font', family='D2Coding')
plt.title('혈액형 비율')
plt.axis('equal')
plt.pie(data, labels=lbl, autopct='%.1f%%',
        colors = color, startangle=90,
        explode=(0, 0, 0.1, 0))
plt.legend()
plt.show()