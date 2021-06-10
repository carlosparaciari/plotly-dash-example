import numpy as np
import matplotlib.pyplot as plt

print("hello planet")

for i in range(4):
    print(i)

x = np.arange(0, 2*np.pi, 0.1)
y = np.sin(x)

plt.plot(x, y)
plt.title('test')
plt.show()
