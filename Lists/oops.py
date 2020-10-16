class Student:
    pass
srikanth=Student()
#variables that are defined outside of the class is instance scope
srikanth.name="Srikanth"#instance variable
srikanth.role="Software Developer"
valli=Student()
valli.name="Valli"
valli.role="Software Developer"
print(srikanth.name,valli.name)

class Employee:
    #class variables are the variables it is defined inside the class
    no_of_leaves=20
    pass
s=Employee()
#class variables are changed in the following ways
print(Employee.no_of_leaves)
s=Employee()
print(s.no_of_leaves)
#Every object has its own set of properties which are accessed 
# using the __dict__ variables which shows the dictionary of properties for that object
print(s.__dict__)
s.no_of_leaves=30
print(s.__dict__)
#values of the class variables will not changed using the instance varible because the 
# instance variable will create new such heap area