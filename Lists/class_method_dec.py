class Student:
    no_of_leaves=8
    @classmethod
    def retValue(cls,defleaves):
        cls.no_of_leaves=defleaves

s=Student()
k=Student.retValue(20)
print(Student.no_of_leaves)

#class method as constructor
class Employe():
    @classmethod
    def values(cls,n):
        return (*(n.split('-')))
k.name=''
k.salary=''
k.leaves=''
k=Employe.values("Srikanth-400-20")
print(k)