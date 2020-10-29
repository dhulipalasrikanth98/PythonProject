import time
def time_delay(n):
    time.sleep(n)
    while True:
        s=(yield)
        with open("new2.txt","r") as f:
            time_delay(6)
            if s in f.readline():
               print("match found......")
            else:
                print("match not found>>>>>!")


s=time_delay(7)
next(s)

s.send(input("enter the the text you want to find"))
s.send(input("enter the the text you want to find"))
s.close()


        
