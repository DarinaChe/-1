import math

from Homework4.func import quadratic_equation


a, b, c = input("Введите числa: ").split()
a = int(a)
b = int(b)
c = int(c)
print(quadratic_equation(a, b, c))

import matplotlib.pyplot as plt
import numpy as np
x_coords = np.linspace(-5, 5, 100)
y_coords = [a*(x_coords**2) + b* x_coords + c for x_coords in x_coords]
plt.plot(x_coords, y_coords )
plt.grid()
plt.show()

