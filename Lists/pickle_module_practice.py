import pickle

file="new.pkl"
f=open(file,'wb')
pickle.dump("srikanth",f)
f.close()
with open(file,'rb') as f:
    print(pickle.load(f))
