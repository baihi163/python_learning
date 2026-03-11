import os
import time
# # # # 'w' 代表 Write（写入模式），encoding='utf-8' 是为了防止中文乱码
# # # with open('my_diary.txt', 'w', encoding='utf-8') as file:
# # #     file.write("这是我用 Python 写下的第一行字！\n")
# # #     file.write("感觉自己像个黑客 😎")
    
# # # # 只要缩进结束，文件就自动安全关闭了！
# # # # 'r' 代表 Read（读取模式），这是默认模式
# # # with open('my_diary.txt', 'r', encoding='utf-8') as file:
# # #     content = file.read()  # 一次性把所有内容读出来
# # #     print(content)3
# # f = open("my_diary.txt",mode='r',encoding='utf-8')
# # # content = f.read()  
# # # print(content)
# # # f.seek(16)
# # # line = f.readline().strip()  # 这时候已经读到文件末尾了，所以返回一个空列表 []
# # # print(line)
# # # line = f.readline().strip()  # 这时候已经读到文件末尾了，所以返回一个空列表 []
# # # print(line)
# # # line = f.readline().strip()  # 这时候已经读到文件末尾了，所以返回一个空列表 []
# # # print(line)
# # # content = f.readlines()  # 这时候已经读到文件末尾了，所以返回一个空列表 []
# # # print(content)
# # for line in f:
# #     print(line.strip())  # strip() 去掉行末的换行符
# # f.close()  # 别忘了关闭文件！
# f = open("baigao.txt",mode='w',encoding='utf-8')
# f.write("kdkkkkkkk\n")
# f.write("dsaddsass\n")
# f.close()  # 别忘了关闭文件！
# lst = ["xiao ming", "xiao gang", "xiao hong"]
# # with open("user_list.txt", "w", encoding="utf-8") as f:#需要把循环写外面
# #     for name in lst:
# #         f.write(name + "\n")  # 每个名字占一行
# f = open("user_list.txt",mode= "a", encoding="utf-8")
# for name in lst:
#     f.write(name + "\n")  # 每个名字占一行
# with open("MaskRCNN_Report.md", "w", encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())  # strip() 去掉行末的换行符

#         f.readlines()  # 这时候已经读到文件末尾了，所以返回一个空列表 []
#         print(content)
with open("人名单.txt", "r", encoding="utf-8") as f1, \
     open("user_list.txt", "w", encoding="utf-8") as f2:
    for line in f1:
        name = line.strip()  # 去掉行首尾空白和换行符
        if name:  # 如果 name 不是空字符串
            f2.write(name + "\n")  # 每个名字占一行
time.sleep(1)  # 模拟一些处理时间            
print("✅ 人名单已成功复制到 user_list.txt！")
os.remove("人名单.txt")  # 删除原文件
os.rename("user_list.txt", "人名单.txt")  # 把新文件重命名为原文件名
print("✅ 已删除原文件并重命名新文件为 人名单.txt！")



    
