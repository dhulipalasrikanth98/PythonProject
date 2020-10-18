class Student:
    no_of_leaves=8
    # def __init__(self,name,salary,role):
    #     self.name=name
    #     self.salary=salary
    #     self.role=role
    @classmethod
    def retValue(cls,defleaves):
        cls.no_of_leaves=defleaves

s=Student()
k=Student.retValue(20)
print(Student.no_of_leaves)

#class method as constructor
class Employe():
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    @classmethod
    def values(cls,n):
        return cls(*(n.split('-')))
j=Employe("srikanth",5775,"developer")

k=Employe.values('Srikanth-5454-developer')
print(k.salary)