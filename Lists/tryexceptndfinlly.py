s=open("newfile.txt")
try:
    f=open("newfile.txt")
except Exception as e:
    print(e)
else:
    print("this will print only after the except")
finally:
    print(s.readline())
    s.close()
    print("it will print defenitly")
