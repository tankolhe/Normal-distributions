import  matplotlib.pyplot as plt
import numpy as np
def X_1(a,b,x):
  if x in range(a,b+1):
    #return a
    return (b-a)
  else:
    return 0

x = np.arange(-100,100,1)
Z = np.vectorize(X_1)(1,3,x)
fig, ax = plt.subplots()
ax.set(xlim=(-4,4), xticks=np.arange(-4,5,1),
       ylim=(0,1),yticks=np.arange(0,1.5,0.5))
plt.plot(x,1/Z)
plt.show()