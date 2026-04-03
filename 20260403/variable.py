#常见数据类型
a = 1
b = 1.0
c = "1"
d = True
print(type(a), type(b), type(c), type(d))

#数据类型转换
a = str(a)
b = int(b)
c = float(c)
print(a, b, c, d)
print(type(a), type(b), type(c), type(d))

#input输入为字符串
age = input("Enter your age: ")
print(age, type(age))
age = int(age)
print(age, type(age))

#拼接字符串：f-string
name = input("Enter your name: ")
print(f"我叫{name}，今年{age}岁")
print("我叫" + name + "，今年" + str(age) + "岁")