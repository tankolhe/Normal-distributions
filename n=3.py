import  matplotlib.pyplot as plt
import numpy as np
def X_3(x):
  if 3<=x<=5 :
    return (x-3)*(x-3)
  if 5<x<=7:
    return (6-2*(x-6)*(x-6))
  if 7<x<=9:
    return (x-9)*(x-9)
  else:
    return 0

x_2 = np.arange(-100,100,1)
Y_1 = np.vectorize(X_3)(x_2)
fig, ax = plt.subplots()
ax.set(xlim=(0,10), xticks=np.arange(0,11,1),
       ylim=(0,1.5),yticks=np.arange(0,1.2,0.2))
plt.plot(x_2,Y_1/16)
plt.show()