### 练习 1：学生信息表
# 用字典存储一个学生的姓名、年龄、成绩，并输出。
name = input("请输入姓名: ")
age = int(input("请输入年龄："))
score = float(input("请输入成绩："))
student = {"name":name,"age":age,"score":score}
print(f"学生档案录入成功！详细信息：{student}")


# ### 练习 2：统计字符串中每个字符出现次数
# 例如： `"hello"` 输出每个字符的次数。
input_string = input()
dictionary = {}
for item in input_string:
    if item not in dictionary:
        dictionary[item] = 1
    else:
        dictionary[item] += 1
print(dictionary)


# ### 练习 3：通讯录小程序
# 实现：# - 添加联系人# - 查询联系人# - 删除联系人
address_book = {}
print("1.添加联系人  2.查询联系人  3.删除联系人  4.退出")
while True:
    condition = input()
    if condition == "1":
        name = input("输入姓名：")
        number = input("输入号码：")
        address_book[name] = number
        print("添加成功！")
    elif condition == "2":
        name = input("输入姓名：")
        if name not in address_book:
            print("查无此人！")
        else:
            print(f"{name}的号码是：{address_book.get(name)}")
    elif condition == "3":
        name = input("输入姓名：")
        del address_book[name]
        print(f"联系人{name}已删除。")
    elif condition == "4":
        print(f"退出通讯录，再见！")
        break
    else :
        continue


# ### 练习 4：商品价格表
# 用字典存商品名和价格，输入商品名后输出价格。
shopping_list = {"可乐": 3.0, "薯片": 6.5, "巧克力": 8.0, "矿泉水": 2.0}
commodity = input()
if commodity in shopping_list:
        print(f"{commodity}的价格是：{shopping_list.get(commodity)}元")
else:
        print(f"抱歉，本店没有出售{commodity}")