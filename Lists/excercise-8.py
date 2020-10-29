import os
def solider_pretty(directory_root,file_name,format):
    with open(file_name,'r') as f:
        p=os.listdir(directory_root)
        s='.txt'
        for i in p:
            if s in i:
                print(i)
        # for i in s:
        #     k=i.split('.')[1]
        #     if k==format:
        #         k=i
        # if s.split('.')[0] not in f.readlines():
        #               s=s[0].upper()+s[1:]
        #               os.rename(i,s)
        # print(os.getcwd(directory_root))
solider_pretty("C://Users/dhuli/Desktop","new2.txt",".jpg")

   