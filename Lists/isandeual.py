a=[1,2,3,4]
b=a
b[0]=7
print(a)
print(b)
print(a==b)
print(a is b)
c=a[:]

print(a==b)
print(a is b)
print(a is c)