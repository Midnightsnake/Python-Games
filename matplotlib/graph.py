import matplotlib.pyplot as plt
import numpy as np
#xValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#yValues = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
xValues = np.linspace(0, 10, 100)
yValues = np.sin(xValues)
plt.figure(figsize = (10, 10))
plt.plot(xValues, yValues, color = "blue")
plt.fill_between(xValues, yValues, color = "red")
plt.show()