f=open('F:/PythonProgramming/Lists/newfile.txt','w')
#write the file use the write() function
#write will replace the file data every time you run
f.write('Write will replace the content\n')
f.close()

#to append the data into the file you have to add 'a' to the open function
f=open('F:/PythonProgramming/Lists/newfile.txt','a')
#How many characters are there in the file it will  print
k=f.write('This append to line2')
print(k)

f.close()
#read and write mode both at a time
f=open('F:/PythonProgramming/Lists/newfile.txt','r+')
print(f.read())
f.write('\nwrite the function')

f.close()