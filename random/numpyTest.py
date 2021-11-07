import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr)

arr1 = np.array([['Oshru', 'Dipto', 'Galib'], ['20141035', '20141036', '20141037']])
data = pd.DataFrame(arr1)
print(data)

x = np.linspace(-2, 5, 50)
y = np.sin(x)
z = np.cos(x)
a = np.tan(x)

plt.plot(x, y)
plt.title('Sine function')
plt.show()

plt.plot(x, z)
plt.title('Cos function')
plt.show()

plt.plot(x, a)
plt.title('Tan function')
plt.show()
