import matplotlib.pyplot as plt

data = [244, 231, 103, 123]
lbl = ['A', 'B', 'AB', 'O']

# 그래프 그리기
plt.axis('equal')
plt.pie(data, labels=lbl)
plt.show()