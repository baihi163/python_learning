# def func(a):
#     print(a)
# d = 10
# func(print(d))
# def func(a):
#     b = pow(a, 2)
#     def inner(b):
#         c = pow(b, 2)
#         print(c)

#     inner(b)


# func(100)
# def func():
#     def inner():
#         print("这是内层函数")
#     inner    
#     return inner
# function = func()
# function() 
# def func(a):
#     a()
# def target():
#     print("这是目标函数")
# func(target)    
# a = 10
def func():
    # a = 20
    # global a
    a = 10
    nonlocal a
    a = 20
func()
print(a)