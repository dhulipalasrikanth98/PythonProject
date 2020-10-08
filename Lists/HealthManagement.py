def getDate():
    import datetime
    return datetime.datetime.now()
def retrive(name):
    name.lower()
    if name=='rohan':
        with open('F:/PythonProgramming/Lists/Rohanhealth.txt') as f:
            print(f.readlines())
        with open('F:/PythonProgramming/Lists/rohanexcercise.txt') as f:
            print(f.readlines())

    elif name=='hammad':
         with open('F:/PythonProgramming/Lists/hammadhealth.txt') as f:
            print(f.readlines())
         with open('F:/PythonProgramming/Lists/hammadexcercise.txt') as f:
            print(f.readlines())
    elif name=='harim':
        with open('F:/PythonProgramming/Lists/harimhealth.txt') as f:
            print(f.readlines())
        with open('F:/PythonProgramming/Lists/harimexcercise.txt') as f:
            print(f.readlines())
        



def inputData():
    t=''
    while t!='x':
        print('Total three clients ')
        print('1.Rohan')
        print('2.Hammad')
        print('3.Harim')
        s=input('Select by pressing the number\n1.Rohan\n2.Hammad\n3.Harim\n')
        if s=='1':
            k=input('Which one you want \n press "e" for excescise "d" for diet\n')
            if k=='d':
                f=open('F:/PythonProgramming/Lists/Rohanhealth.txt','a')
                f.write('\n')
                f.write(str(getDate()))
                f.close()
                f=open('F:/PythonProgramming/Lists/Rohanhealth.txt','a')
                print("Enter your diet for today")
                f.write(input())
                f.close()
                t=input('do you want to continue press c or x for exit\n')
        
            elif k=='e':
                f=open('F:/PythonProgramming/Lists/rohanexcercise.txt','a')
                f.write('\n')
                f.write(str(getDate()))
                f.close()
                f=open('F:/PythonProgramming/Lists/rohanexcercise.txt','a')
                print("Enter your Excercises for today")
                f.write(input())
                f.close()
                t=input('do you want to continue press c or x for exit\n')
        if s=='2':
            k=input('Which one you want \n press "e" for excescise "d" for diet\n')
            if k=='d':
                f=open('F:/PythonProgramming/Lists/hammadhealth.txt','a')
                f.write('\n')
                f.write(str(getDate()))
                f.close()
                f=open('F:/PythonProgramming/Lists/hammadhealth.txt','a')
                print("Enter your diet for today")
                f.write(input())
                f.close()
                t=input('do you want to continue press c or x for exit\n')
            elif k=='e':
                f=open('F:/PythonProgramming/Lists/hammadexcercise.txt','a')
                f.write('\n')
                f.write(str(getDate()))
                print("Enter your diet for today")
                f.write(input())
                f.close()
                t=input('do you want to continue press c or x for exit\n')
        if s=='3':
            k=input('Which one you want \n press "e" for excescise "d" for diet\n')
            if k=='d':
                f=open('F:/PythonProgramming/Lists/harimhealth.txt','a')
                f.write('\n')
                f.write(str(getDate()))
                print("Enter your diet for today")
                f.write(input())
                f.close()
                t=input('do you want to continue press c or x for exit\n')
            elif k=='e':
                f=open('F:/PythonProgramming/Lists/harimexcercise.txt','a')
                f.write('\n')
                f.write(str(getDate()))
                print("Enter your excecise for today")
                f.write(input())
                f.close()
                t=input('do you want to continue press c or x for exit')


print('Welcome to health management System')
c=''
s=1
while c!='x' and s!=3:
    c=input('Enter c to continue xto exit\n')
    s=int(input('enter 1.inputData\n2.getData\n3.exit\n'))
    if s==1:
        inputData()
        c=input('Do you want to continue c to continue and x for exit?\n')
    elif s==2:
        l=''
        while l!='x':
            l=input('enter rohan or hammad or hamir to continue and x for exit\n')
            retrive(l)
    elif s==3:
        c='x'
print('Thank you for visiting')




        