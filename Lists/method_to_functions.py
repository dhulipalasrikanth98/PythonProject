class A:
    def __init__(self,name,salary,years):
        self.name=name
        self.salary=salary
        self.years=years
    def __add__(self,others):
        return self.salary+others.salary
    def __gt__(self,others):
        return self.salary>others.salary
    def __ge__(self,others):
        return self.salary>=others.salary
    def __ne__(self,others):
        return self.salary!=others.salary
    def __getitem__(self,key):
        return self.years[key]
    def __delitem__(self,key):
        del self.years[key]
    # def deleteitem(self,key):
    #     return __delitem__(key)

    def __repr__(self):
        return f"A(name:'{self.name}',salary{self.salary},years{self.years})"

k=A("srikanth",4433,[1994,1995,1996])
m=A("valli",675986,[12345,45678,9087])
print(k+m)
print(k>m)
print(k>=m)
print(k!=m)
del k.years[2]
print(k)
