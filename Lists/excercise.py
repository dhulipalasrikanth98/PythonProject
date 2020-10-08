n=int(input())
k=input('Enter false for reverse and True for not reverse:\t')
k.lower()
if k=='true':
    for i in range(0,n):
        for j in range(0,i+1):
            print('*',end=' ')
        print()
else:
    for i in range(n-1,-1,-1):
        for j in range(i,-1,-1):
            print('*',end=' ')
        print()