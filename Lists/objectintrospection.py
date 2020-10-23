#object interospection is nothing but displying what methods or what varibles are calling or can use
class A:
    def __init__(self,a,b) -> None:
       
        self.a=a
        self.b=b
    def __eq__(self, o: object) -> bool:
        return self.a==o.a
    

    

a1=A("srikanth","valli")
a2=A("srikanth","valli")
print(a1==a2)
import inspect
print("inspect.getmembers(a1)",'\n',inspect.getmembers(a1))
print("inspect.getmodule(a1)",'\n',inspect.getmodule(a1))
print("inspect.ismodule(a1)",inspect.ismodule(a1))
print(inspect.Parameter(a1))
