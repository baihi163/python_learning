class Student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say(self):
        print("我叫%s,今年%d岁了,性别是%s"%(self.name,self.age,self.gender))
    def write(self):
        print(f"{self.name}{self.age}岁喜欢写代码")

s1 = Student("小明",18,"男")
s1.say()
s1.write()
s2 = Student("bai",19,"男")
s2.say()
s2.write()