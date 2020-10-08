#with syntax is with open(filepath) as f
#as means alias of the file
with open('F:/PythonProgramming/Lists/newfile.txt') as f:
    a=f.readlines()
    print(a)
f=open('F:/PythonProgramming/Lists/newfile.txt')
print(f.readlines())
f.close()
