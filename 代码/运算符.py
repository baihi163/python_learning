# # # a = 10
# # # b = 3
# # # c = a % b
# # # print(c)  # 输出 1，因为10除以3的余数是1
# # # # n = int(input("请输入一个整数: "))
# # # # if n % 2 == 0:
# # # #     print(f"{n} 是偶数")
# # # # else:
# # # #     print(f"{n} 是奇数")
# # # d = a // b
# # # print(d)  # 输出 3，因为10除以3的商是3（整数部分）
# # # e = a ** 5  
# # # print(e)  # 输出 1000，因为10的3次方是1000
# # a = 10
# # b = 3
# # # print(a == b)
# # # print(a != b)
# # # print(a > b)    
# # a,b =b,a
# # print(a) 
# # print(b)
# age = int(input("请输入您的年龄: "))
# has_id = input("请问您带了身份证吗？（是/否）: ")

# # 🌟 核心修改：直接判断文字是否等于 "是"
# if (age >= 18) and (has_id == "是"):
#     print("欢迎光临！")
# else:
# #     print("未成年或未带证件，禁止入内！") 
# banned_users = {"xiao ming", "xiao gang"}
# current_user = "xiao hong"

# # 如果当前用户 不在 黑名单里
# if current_user not in banned_users:
#     print("欢迎登录！")
# else:
#     print("账号被封禁！")
# 假设用户直接敲了回车，什么都没输入
user_name = input("请输入用户名：")  # 此时 user_name 是 "" (空字符串)

# 🌟 神技：如果 user_name 是空的 (False)，not 会把它变成 True，从而触发报错提示
if not user_name:
    print("用户名不能为空，请重新输入！")
else:
    print(f"欢迎你，{user_name}！")


