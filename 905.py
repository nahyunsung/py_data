import matplotlib.pyplot as plt

plt.title('color')
plt.plot([10, 20, 15, 5], color='white', label='a')
plt.plot([30, 20, 26, 23], color='black', label='b')
plt.legend(loc='best')
plt.show()