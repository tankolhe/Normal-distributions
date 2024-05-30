import  matplotlib.pyplot as plt
import numpy as np
def X_2(a):
  if 2<=a<4:
    return (a-2)
  if 4<=a<=6:
    return (6-a)
  else:
    return 0
x_1 = np.arange(-100,100,1)
Y = np.vectorize(X_2)(x_1)
fig, ax = plt.subplots()
ax.set(xlim=(0,10), xticks=np.arange(0,11,1),
       ylim=(0,1.5),yticks=np.arange(0,1.2,0.2))
plt.plot(x_1,Y/4)
plt.show()