class A:
    def met(self,name):
        print("this is from class A")
        self.name=name
        print(f"{self.name}")
class B(A):
    def met(self,name):
        print("this is from class B")
        self.name=name
        print(f"{self.name}")
class C(A):
    def met(self,name):
        super().met("hi")
class D(C,B):
    pass
s=D()
s.met("hi")
    