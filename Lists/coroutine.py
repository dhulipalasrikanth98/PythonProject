import time
def readFile():
    s="this is srikanth learning python programming"
    time.sleep(4)

    while True:
        value = (yield)
        if value in s:
            print("Value is in the string")
        else:
            print("value is not in the string")
val = readFile()
print("readfile started......................")
next(val)
val.send("srikanth")
val.close()
val=readFile()
next(val)
val.send("this")
