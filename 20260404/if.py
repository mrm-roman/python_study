### 练习 1：判断奇偶数
#输入一个整数，判断是奇数还是偶数。
number = int(input("enter number: "))
if number%2 == 0:
    print(f"{number}是偶数")
else:
    print(f"{number}是奇数")

### 练习 2：成绩等级
#输入成绩：- 90 及以上：A - 80~89：B - 70~79：C - 60~69：D - 60 以下：E
score = float(input("Enter your score: "))
if score >= 90:
    print(f"{score} gets A")
elif score >= 80:
    print(f"{score} gets B")
elif score >= 70:
    print(f"{score} gets C")
elif score >= 60:
    print(f"{score} gets D")
elif score>=0 and score<60:
    print(f"{score} gets E")
else:
    print(f"{score}输入错误")

### 练习 3：判断闰年
#规则：- 能被 400 整除，或者能被 4 整除但不能被 100 整除
year = int(input("Enter the year: "))
if (year%400 == 0) or (year%4 == 0 and year%100 != 0):
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")

### 练习 4：简单计算器
#输入两个数和运算符，输出结果。
number1 = float(input("Enter your number1: "))
number2 = float(input("Enter your number2: "))
operator = input("Enter your operator: ")
if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
elif operator == "%":
    print(number1 % number2)
elif operator == "//":
    print(number1 // number2)
elif operator == "**":
    print(number1 ** number2)
else:
    print("Sorry, we can\'t calculate that. ")