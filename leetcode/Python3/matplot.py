import matplotlib
import numpy as np

x = np.arange(0,100)
y = x*2
z = x**2

import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,.5,.2,.2])
ax1.plot(x,y)
ax2.plot(x,y)
plt.show()