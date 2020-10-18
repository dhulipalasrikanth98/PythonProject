# def func(func1):
#     func1()
# def func1():
#     print("this is srikanth")
# func(func1)

# def func1(func2):
#     func2("this")
# func1(print)


#*********decorator concept*************#
def func1(func):
    def ex():
        print("how are you")
        func()
        print("this is srikanth")
    return ex

# def this_is_srikanth():
#     print("who is this")
# this_is_srikanth = func1(this_is_srikanth)
# this_is_srikanth()
@func1
def this_is_srikanth():
    print("srikanth")
this_is_srikanth()
