### 练习 1：1 到 100 求和
from unittest import result

sum = 0
for i in range(101):
    sum = sum + i
print(sum)


### 练习 2：输出 1 到 100 的偶数
for i in range(101):
    if((i%2==0) and (i!=0)):
        print(i)


### 练习 3：猜数字游戏
#设定一个答案，让用户不断输入，直到猜对为止。
number = 32
while True:
    guess_number = int(input("Enter a number between 0 and 100: "))
    if guess_number == number:
        print("你猜对了！！！")
        break
    elif guess_number < number:
        print("你猜小了")
        pass
    elif guess_number > number:
        print("你猜大了")
        pass


### 练习 4：打印九九乘法表
for row in range(1,10):
    for col in range(1,row+1):
        print(f"{row} x {col} = {row*col}", end="\t")
    print()


### 练习 5：统计字符串中某个字符出现次数
#例如统计 `"banana"` 中 `'a'` 的个数。
input_str = input("Enter a string: ")
input_want = input("Enter a word: ")
str_number = 0
for char in input_str:
    if char == input_want:
        str_number = str_number + 1
print(str_number)
