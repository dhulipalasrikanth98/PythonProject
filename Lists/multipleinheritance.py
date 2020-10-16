class ElectronicDevice:
    device_name="floppydisk"
    def __init__(self,cost):
        self.cost=cost
class telephone(ElectronicDevice):
    device_name="telephone"
    def __init__(self,cost):
        self.cost=cost
    def printbrand(self):
        return f"the brand is bsnl "
class mobilephone(telephone):
    device_name="samsung"
    def __init__(self,cost):
        self.cost=cost
    def printvalues(self):
        return f"the mobile phone cost is {mobilephone.device_name}{self.cost}"
k=mobilephone(18499)
print(k.printvalues())

                                                            




