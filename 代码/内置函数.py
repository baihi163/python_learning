# # # a = 46
# # # b = 5
# # # print(pow(a,b))
# # lst = [1, 2, 3, 4, 5]
# # print(sum(lst))
# # print(max(lst))
# # print(min(lst))
# s = {1, 2, 3}
# lst = list(s)
# print(lst)
# t = tuple(s)
# print(t)
# a = 10
# print(format(18, "08b"))
# a = "白"
# print(ord(a))
# print(chr(30333))
# fruits = ["苹果", "香蕉", "橘子"]

# # 使用 enumerate：直接同时拿到序号 (i) 和元素 (fruit)
# for i, fruit in enumerate(fruits):
#     print(f"第 {i} 个水果是 {fruit}")
# lst = [1, 2, 3, 4, 5]
# tuple = (1, 2, 3, 4, 5)
# dict = {"a": 1, "b": 2, "c": 3}
# # print(hash(lst))
# print(hash(tuple))
# # print(hash(dict))
# 场景：存储游戏角色的属性
# player = {
#     ""name": "亚瑟",\n
#     "hp": 3000,\n
#     "skills": ["圣剑裁决", "誓约之盾"]"" # 值可以是列表
# }
# print(player)  # 瞬间查到血量：3000
import pprint

# 1. 标准定义字典（不要管代码里怎么换行，不要加 \n）
player = {
    
    "skills": ["圣剑裁决", "誓约之盾"]
}

# 2. 瞬间查血量（字典的超能力保留了！）
print("当前血量：", player["hp"]) 

# 3. 漂亮地打印整个字典
pprint.pprint(player)
print(help(pprint.pprint))
print(dir(hash))