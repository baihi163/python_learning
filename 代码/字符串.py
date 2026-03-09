# # # # # # # s = "我叫柏高是的撒旦撒旦"
# # # # # # # print(s[0])
# # # # # # # print(s[3:5])
# # # # # # # print(s[3:])
# # # # # # # print(s[:5])
# # # # # # # print(s[-1])
# # # # # # # print(s[-3:-1])
# # # # # # # print(s[-3:])
# # # # # # # print(s[:-3])
# # # # # # # print(s[0:5:2])
# # # # # # # print(s[::2])
# # # # # # s ="python"
# # # # # # s1 =s.capitalize()
# # # # # # print(s1)
# # # # # a = "你好， 我叫白高"
# # # # # a2 = a.replace("白高","小明")
# # # # # print(a2)
# # # # # a3 =a.replace(" ","")
# # # # # print(a3)


# # # # a = "  love1 luv11 flower"
# # # # a1 = a.split()
# # # # print(a1)
# # # # a2 = a.strip()
# # # # print(a2)
# # # # a = "hello world" 
# # # # a1 = a.find(" ")
# # # # print(a1)   
# # # a2 = "你好，我叫白高"
# # # a3 = a2.find("白高123")
# # # print(a3)
# # # a4 = a2.index("白高123")
# # # print(a4)


# # money = input("请输入金额：")
# # if money.isdigit():
# #     money = int(money)
# #     if money >= 100:
# #         print("你有100块钱了")
# #     else:
# #         print("你没有100块钱")
# # else:
# #     print("请输入数字")        



# name = input("请输入名字：")
# if name.startswith("小"):
#     print("名字以小开头")
#     if name.endswith("明"):
#      print("名字以明结尾")
#     else:
#      print("name is not true")
# else:    
#     print("name is not true")


a = ['a','b','c']
a1 = "-".join(a)
print(a1)
a2 ="".join(a)
print(a2)
len(a)
print(len(a))