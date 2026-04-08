### 练习 1：定义一个函数，返回两个数的和
def add_numbers(num1, num2):
    return num1 + num2
print(add_numbers(3, 5))
print(add_numbers(-1.5, 2.5))


### 练习 2：定义一个函数，判断一个数是否为素数
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(3, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))
print(is_prime(9999991))
print(is_prime(1))


### 练习 3：定义一个函数，计算阶乘
def calculate_factorial(n):
    if (n == 1) or (n == 0):
        return 1
    return n * calculate_factorial(n-1)
print(calculate_factorial(5))
print(calculate_factorial(0))

### 练习 4：写一个函数，输入列表，返回最大值
def find_max(numbers):
    numbers.sort()
    return numbers[-1]
print(find_max([1, 5, 3, 9, 2]))
print(find_max([-5, -10, -2, -1]))


### 练习 5：封装“成绩等级判断”函数
def get_grade_level(score):
    if 90 <= score <= 100:
        return "A"
    if 80 <= score <= 89:
        return "B"
    if 70 <= score <= 79:
        return "C"
    if 60 <= score <= 69:
        return "D"
    if 0 <= score <= 59:
        return "E"
    else:
        return "无效成绩"
print(get_grade_level(95))
print(get_grade_level(72.5))
print(get_grade_level(59))
print(get_grade_level(105))
