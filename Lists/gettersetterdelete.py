class A:
    def __init__(self,fname,lname) -> None:
        self.fname=fname
        self.lname=lname
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@google.com"
    @email.setter
    def email(self,string):
        names=string.split('@')[0]
        self.fname=names.split('.')[0]
        self.lname=names.split('.')[1]
    
    
a=A("srikanth","venkatesa")
# print(a.printvalues())
print(a.email)
print(a.fname)
a.email="this.that@google.com"

