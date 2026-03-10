# # # # s = {1,2,5,"xi",([1,2,3],1)}
# # # # print(s)
# # # s = set()
# # # print(s)
# # # s.add(1)
# # # print(s)
# # # s.remove(1)
# # # s.add(1)
# # # s.add(2)
# # # print(s)
# # # s.add(1)
# # # s.remove(1)
# # # print(s)
# # s = {2}

# # s.add(1)     # 集合变成 {1, 2}
# # s.remove(1)  # 成功找到并删除 1，集合变回 {2}，不报错
# # s.discard(1)  # 尝试删除 1，但集合里已经没有 1 了。discard 不会报错，集合仍然是 {2}
# # print(s)     # 输出 {2}
# # # 🌟 见证报错的时刻：
# # # s.remove(1)  # 再次尝试删除 1。但此时集合里只有 2 了，找不到 1！
# # # 💥 此时就会瞬间触发：KeyError: 1
# # for item in s:
# #     print(item)  # 输出集合中的每个元素
# s1 = {"xiao ming", "xiao hong"}
# s2 = {"xiao ming", "xiao gang"}
# print(s1 & s2)  # 输出 s1 和 s2 的交集：
# print(s1 | s2)  # 输出 s1 和 s2 的并集：
# print(s1.union(s2))  # 输出 s1 和 s2 的并集（另一种写法）：
# print(s1 - s2)  # 输出 s1 和 s2 的差集：
# print(s1.difference(s2))  # 输出 s1 和 s2 的差集（另一种写法）：
s1 = {"xiao ming", "xiao hong"}
print(s1)
s1.add("xiao ming")
print(s1)

lst = ["xiao ming", "xiao hong", "xiao ming", "xiao gang"]
print (lst)
print(set(lst))