import numpy as np
a=np.array([5,1,7])
b=np.zeros(2)
c=np.ones(2)
a=np.sort(a)
#reshape the array u have to use the array_name.reshape(xand y axis)
k=a.reshape(2,3)
print('a',k,'\n','b',b,'\n','c',c)