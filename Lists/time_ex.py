import time
#it will return the number of ticks
i=time.time()
for i in range(6):
    print(i)
print(time.time()-i)
k=0
i2=time.time()
while k<6:
    print(k)
    k=k+1
print(time.time()-i2)
print(time.asctime(time.localtime(time.time())))