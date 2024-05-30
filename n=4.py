import  matplotlib.pyplot as plt
import numpy as np
def X_4(a):
  if 4<=a<=6:
    return (a-4)**3
  if 6<a<=8:
    return (8 - (a-6)**3 + 18*(a-6) -2*((a-7)**3 - 1))
  if 8< a <=10:
    return (18*(10 - a) -2*(1 - (a -9)**3) + (a-10)**3 +8)
  if 10< a <=12:
    return (12 - a)**3
  else:
    return 0
  
x_3=np.arange(-100,100,1)
Y_2 = np.vectorize(X_4)(x_3)
fig, ax = plt.subplots()
ax.set(xlim=(0,15), xticks=np.arange(0,16,1),
       ylim=(0,1),yticks=np.arange(0,1.2,0.2))
plt.plot(x_3,Y_2/96)
plt.show()