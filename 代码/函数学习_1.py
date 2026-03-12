# def my_function(name,lvl):
#     """这是一个简单的函数示例"""
#     print("Hello, World!", name, "Your level is", lvl)

# name = "Alice"
# lvl = 5
# my_function(name, lvl)  # 调用函数
# # 
# def my_function(name, gender, lvl, role):
#     print(f"玩家：{name}，性别：{gender}，等级：{lvl}，职业：{role}")

# name = input("请输入玩家姓名：")
# gender = input("请输入玩家性别：")
# lvl = int(input("请输入玩家等级："))
# role = input("请输入玩家职业：")
# my_function(name, gender, lvl, role)  # 调用函数
# def build_profile(name, **info):
#     print(f"姓名：{name}")
#     print(f"其他信息：{info}")

# build_profile("Alice", age=25, city="上海", job="法师")
# 输出：
# 姓名：Alice
# 其他信息：{'age': 25, 'city': '上海', 'job': '法师'}
# def build_profile(name,*sss,lvl=0,**info):
#     print(f"姓名：{name}等级：{lvl}",sss,info)
# build_profile("Alice", 5, 1, 2, 3, role="战士", age=25,lvl=10, city="上海", job="法师")
# def bai_fen(*args, **kwargs):
#     print(args, kwargs) 
# bai_fen(1, 2, 3, name="Alice", age=25)
# ori_list = [1, 2, 3, 4, 5]
# def modify_list(*a):
#     print("原始列表:", a)
# modify_list(*ori_list)
# def func(a, d):
#     return a + d
# result = func(5, 10)
# print(result)
def func(a, d):
    return a, 1, 2 
function = func(5, 10)
   