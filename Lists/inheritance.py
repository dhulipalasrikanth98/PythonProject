class Employee:
    def __init__(self,name,amount)->None:
        self.name=name
        self.amount=amount
    
    def retvalues(self):
        return f"the name of the persion {self.name}and salary is{self.amount}"
    @classmethod
    def changeamount(self,a):
        self.amount=a
        return self.amount
    # @staticmethod
    # def printvalues(self):
    #     return f"values are {self.name},{self.amount}"
class Person(Employee):
    pass

k=Person("Srikanth",99809809)
print(k.retvalues())
k.amount=k.changeamount(700)
print(k.retvalues())
print(k.__dict__)
print(k.printvalues())


