import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 30)
print(x)
plt.plot(x, x**2, 'r', x, x*np.log2(x), 'g', x, x, 'b', x, np.log2(x), '--')
plt.legend(['x^2', 'n lg n', 'n', 'lg n'])
plt.show()
