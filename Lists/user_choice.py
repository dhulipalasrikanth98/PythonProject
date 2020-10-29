def list_comprehensions():
    print("Welcome to list comprehensions")
    s=int(input("Enter the rnge of values to generate"))
    k=[i for i in range(s)]
    print(k)
       
def set_comprehension():
    print("Welcome to set comprehensions")
    print("You can enter the duplictes and see the magic")
    s=int(input("How many inputs you want to enter"))
    k={input() for i in range(s)}
    print(k)
def dictionary_comprehensions():
    print("Welcome to dictionary comprehensions")
    j=int(input("How many key value pairs you want to give enter key in first line and value in the next line"))
    f={input():input() for i in range(j)}
    print(f)
print("Welcome to comprehensions")
while(True):
    k=input("Enter your comprehension type \n 1. List comprehensions 2. dictilnary comprehensions 3. set comprehensions")
    if k=="1":
        list_comprehensions()
        t=input("Do you want to exit from the press c")
        if t=='c':
            break
    elif k=='2':
        dictionary_comprehensions()
        t=input("Do you want to exit from the press c")
        if t=='c':
            break
    elif k=='3':
        set_comprehension()
        t=input("Do you want to exit from the press c")
        if t=='c':
            break
print("Thank you for using comprehensions")

        
