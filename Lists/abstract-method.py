# from abc import ABC,abstractmethod#3.4 or higher versions
from abc import ABCMeta,abstractmethod#3.8 or higher versions
class superior(metaclass=ABCMeta):
    @abstractmethod
    def printmethod():
        return 0

class A(superior):
    # def __init__(self,name,salary,role):
    #     self.name=name
    #     self.salary=salary
    #     self.role=role
    @classmethod
    def printmethod(self):
        return "this is srikanth"
a=A()
print(a.printmethod())
print("hello")