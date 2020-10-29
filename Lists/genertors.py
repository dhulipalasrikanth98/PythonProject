def genrating(input):
    for i in range(input):
        yield i
s=genrating(300)



k="srikanth"
l=iter(k)
print(l.__next__())
# for i in l:
#     print(i)