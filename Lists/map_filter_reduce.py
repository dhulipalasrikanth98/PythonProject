#****************Map*********************#
l=["1","2","3","4"]
k=list(map(int,l))
m=list(map(lambda f:f%2,k))
print(m)

#*****************Filter*****************#
l=[21,30,40,50]
f=list(filter(lambda x:x%2==0,l))
print(f)

#*******************reduce***************#
from functools import reduce
s=[3,4,5,7]
j=int(reduce(lambda x,y:x+y,s))
print(j)
