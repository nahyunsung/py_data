import matplotlib.pyplot as plt

plt.title('legend')
plt.plot([1, 2, 3, 4], label='a')
plt.plot([10, 20, 20, 20], label='b')
plt.legend()
plt.show()