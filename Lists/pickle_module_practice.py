import pickle

file="new.pkl"
with open(file,'rb') as f:
    print(pickle.load(f))
