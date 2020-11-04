#1->2->3
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class SLinked:
    def __init__(self):
        self.headVal=None
    # def createLinkedList(self,datas):
    #     if self.headVal is None:
    #         self.headVal=Node(data,None)
            # return;
    def print(self):
        l=self.headVal
        while l.next:
            print(l.data)
            l=l.next
        print(l.data)
    # def createLinkedList(self,data):
    #     if self.headVal is None:
    #         self.headVal=Node(data,None)
    def add_begining(self,data):
        n=Node(data,self.headVal)
        if self.headVal==None:
            self.headVal=Node(data,None)
        self.headVal=n
    def add_end(self,data):
        if self.headVal==None:
            self.headVal=Node(data,None)
        l=self.headVal
        while l.next:
            l=l.next
        l.next=Node(data,None)
    def remove_beg(self):
        if self.headVal is None:
            print("No value create the data")
        l=self.headVal
        l=l.next
        self.headVal=l
    def remove_end(self):
        if self.headVal is None:
            print("No values")
        else:
             l=self.headVal
             l=l.next
             while l.next:
                 if l.next.next is None:
                     break;
                 l=l.next
             l.next=None
            
        
       

    

    
            
new_node = SLinked()
new_node.add_begining(7)
new_node.add_begining(4)
new_node.add_begining(3)
new_node.add_begining(2)
new_node.add_begining(1)
new_node.add_begining(5)
new_node.print()
new_node.remove_beg()
print("After removing the beg value")
new_node.print()
print("After removing the beg value")
new_node.remove_beg()
new_node.print()
print("After removing the end value")
new_node.remove_end()
new_node.print()

