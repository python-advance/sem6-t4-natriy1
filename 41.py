import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

data = pd.read_csv('web_traffic.tsv', sep='\t', header=None)

x, y = data[0], data[1]

x_list = list(x)
y_list = list(y)

for i in range(len(y_list)):
    if math.isnan(y_list[i]):
        y_list[i] = 0
    else:
        y_list[i] = y_list[i]

x1 = [1, 743]

np_x = np.array(x_list)
np_y = np.array(y_list)

x2 = list(range(743))

plt.scatter(x_list, y_list, label = u'Исходные данные', color='purple')

f3 = sp.poly1d(np.polyfit(np_x, np_y, 3))
plt.plot(x2, f3(x2), linewidth = 2, label = u'полином 3-ей степени')
f4 = sp.poly1d(np.polyfit(np_x, np_y, 4))
plt.plot(x2, f4(x2), linewidth = 2, label = u'полином 4-ой степени')
f10 = sp.poly1d(np.polyfit(np_x, np_y, 10))
plt.plot(x2, f10(x2), linewidth = 2, label = u'полином 10-ой степени')

plt.title('Линейная регрессия')
plt.legend()
plt.ylabel('y')
plt.xlabel('x')
plt.show()
