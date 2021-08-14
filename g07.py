import matplotlib.pyplot as plt

plt.title('maker')
plt.plot([10, 20, 30, 40], '.', label='circle', linestyle='--')
plt.plot([40, 30, 20, 10], '^', label='triangle', linestyle='-.')
plt.legend(loc='best')
plt.show()