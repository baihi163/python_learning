# # # a =['a','b','c',1,2,3]
# # lst = ['a','s','d','f','d']
# # print(lst)
# # print(lst[0:3])
# # for itn in lst[0:3:2]:
# #     print(itn)
# # len(lst)
# # print(len(lst)) 
lst =[]
lst.append("baigao")
lst.append("chegan")
#print(lst)
lst.insert(1,"xiao ming")
#print(lst)  
lst.extend(["xiao hong","xiao hua"])
# # print(lst)
# # ret = lst.pop(3)
# # print(lst)
# # print(ret)
# # lst.remove("xiao ming")
# # print(lst)
# # lst[2] = "hihi"
# # print(lst)
# print(lst[1:4])
# # for itn in lst :
# for i in range(len(lst)):
#     itn = lst[i]
#     if itn.startswith("xiao"):
#        inm = "bai"+itn[4:]
#        print(inm)
#        lst[i] = inm
# print(lst)
# lst.sort()
# lst.insert(0,[114,514,[1991,"baigao"]])
# print(lst)
# print(lst[0][2][1])
# lst[0][2][1] = lst[0][2][1].upper()
# print(lst)
temp = []
for i in lst:
    if i.startswith("bai"):
        temp.append(i)
        for j in temp:
            lst.remove(j)
print(lst)
        


       