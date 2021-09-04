import matplotlib.pyplot as plt

plt.title('linestyle')
plt.plot([10, 20, 15, 23], label='dashed', linestyle='--')
plt.plot([40, 30, 20, 10], label='dotted', linestyle=':')
plt.legend(loc='best')
plt.show()