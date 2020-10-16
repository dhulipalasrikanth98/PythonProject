class Student:
   
    def __init__(self,name,salary) -> None:
        self.name=name
        self.salary=salary
    def details(self,func):
      func(f"student details name:{self.name} salary {self.salary}")


h=Student("valli",2500000000000000000000000)
h.details(print)

