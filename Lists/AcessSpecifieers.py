class Employee:
    var=10
    _p=20#protected variable
    __c=30
    
    
f=Employee()
print("public")
print(f.var)
print("protected")
print(f._p)
print("priavte variable")
print(f._Employee__c)
