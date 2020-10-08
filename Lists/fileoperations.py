#defalut mode for the file is read and rt
#open will return a pointer (or file handler) for the file
f=open('F:/PythonProgramming/Lists/newfile.txt','rt')


#read first 3 charcters in the file
#content = f.read(3)
#print("file data")


#donot read the file if you want to print the file line by line donot use 
# f.read() before exceuting the function
#for i in f:
    #print(i,end="")


#readline() function will print the single line of the file each time
print(f.readline())
print(f.readline())
print(f.readline())
#best practice is to close the file if it is open
f.close()
k=open('F:/PythonProgramming/Lists/newfile.txt')
#readlines will print the file data into a list
print(k.readlines())
#best practice is to close the file if it is open
k.close()

f=open('F:/PythonProgramming/Lists/newfile.txt')
#tell and seek
#tell will tell the current positiom
print(' the current position of the file',f.tell())
print(f.readline())
print('the current position of the file',f.tell())
#seek() will reset the file pointer to the given position f.seek(integervalue)
f.seek(20)
print('the current position of the file',f.tell())
#if you put the seek to the given position then the file will start read from that line
print(f.readline())

f.close()

