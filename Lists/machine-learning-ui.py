import requests
import pickle
s=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
l=input('Enter the file you want to pickle')
t=l+'.pkl'
j=list(s.text.split('\n'))

f=open(t,'wb')
pickle.dump(j,f)
f.close()
print(the file data)
with open(t,'rb') as g:
    print(pickle.load(g))


