import matplotlib.pyplot as plt

data = [70, 50, 60, 80, 95, 75]
lbl_x = [f'{one+1}학년' for one in range(6)]

plt.style.use('ggplot')
plt.rc('font', family='D2Coding')
plt.figure(figsize=(10, 8), dpi=72)
plt.title('가로막대 그래프')
plt.barh(lbl_x, data)
plt.show()