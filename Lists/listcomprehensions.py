#list comprehensions
l=[i for i in range(30) if i%2==0]
print(l)
#dictionary comprehension
dict1 ={i:f"this is srikanth{i}" for i in range(5)}
print(dict1)
dict1={i:j for j,i in dict1.items()}
print(dict1)
#  value1 ={i for i in range(200)}
#set comprehensions
val={"srikanth","srikanth"}
print(type(val))

#generators comprehension
e =(i for i in range(2000))
print(e.__next__())
#it is geneally used for the iter type means iterator
k="srikanth"
s=iter(k)
print(s.__next__())


# for i in e:
#     print(i)