# python_study（2026年4月：python入门学习）
学习目录框架:
1. 开发环境与基本运行方式
2. 变量、数据类型、输入输出
3. 运算符与条件判断
4. 循环：for / while
5. 字符串
6. 列表
7. 字典
8. 函数入门


## 学习环境：
- 电脑：Windows11系统 / MacOS系统
- 解释器版本：python 3.12.10    
    https://www.python.org/downloads/release/python-31210/
- 代码编辑器/IDE：Pycharm2026.1    
    https://www.jetbrains.com/zh-cn/pycharm/


## 2026.4.2
1. 学会在github上创建仓库，撰写README，提交代码
2. 从官网下载安装python解释器3.12.10
3. 从官网下载安装pycharm2026.1（PS：在网页下载慢，把下载链接复制到迅雷会很快）
4. 打开pycharm，创建自己的第一个项目python_study
5. 在该项目下创建第一个python代码，helloworld
- 【总结】：完成“开发环境与基本运行方式”，“变量、数据类型、输入输出”中的各种print用法

## 2026.4.3
1. 变量（variables）是什么？可以赋给值的标签
2. 变量命名：只能字母开头，由字母+数字+下划线构成。通常用英文起名，原空格用下划线代替。
3. 变量赋值：=
4. 常见数据类型：
    - 整数 `int`
    - 浮点数 `float`
    - 字符串 `str`
    - 布尔值 `bool`
5. 查看数据类型：`type()`
6. 类型转换：
```python
    int("123")
    float("3.14")
    str(100)
```
7. 输出：`print()`
    - 在 Python 中，print() 函数在默认情况下会在末尾自动帮你敲回车。也就是说，当你写下`print("你好")`时，Python 实际上执行的是`print("你好", end="\n")`。end是print函数里的一个特殊参数，它的意思是：“打印完这句话之后，最后要加点什么？”，当你手动写了 end="..." 时，Python 就会听你的，不再偷偷敲回车了。
    - 
  
 
    - 输入：`input()`    注意：`input()` 得到的是字符串
    > 为什么 input() 默认得到的是字符串？          
    > 不自作主张，把input进来的所有内容当作纯粹的静态文本对待，保障程序安全和避免用户数据丢失。

9. 格式化输出：
    - 拼接字符串和变量 `f-string`
```python
    name = "小明"
    age = 18
    print(f"我叫{name}，今年{age}岁")
    print("我叫" + name + "，今年" + str(age) + "岁")  # 变量age需要转换成字符串，因为只有字符串才能连接字符串
```
- 【总结】：完成“变量、数据类型、输入输出”

## 2026.4.4
1. 算术运算符
    - `+ - * /`
    - `//` 整除
    - `%` 取余
    - `**` 幂运算
2. 比较运算符：单一判断
    - `>  <  >=  <=  ==  !=`
3. 逻辑运算符：将单一判断组合为多条件复杂判断
    - `and`：（且）只有当 and 两边的条件全都是 True 时，最终结果才是 True
    - `or`：（或）只要 or 两边的条件中哪怕有一个是 True，最终结果就是 True
    - `not`：（取反）翻转结果的。把 True 变成 False，把 False 变成 True
4. 条件判断
    - `if:...`
    - `if:...else:...`
    - `if:...elif:...else:...`
    - ps：`elif`可使用多次；`else`可省略；`if...elif...else`结构在一个条件通过执行后将跳过余下的其余条件。
5. for循环：`for 临时变量 in 可迭代对象:`
    - 可迭代对象通常是列表、字符串或者 range() 生成的一组数字
    - 遍历列表：
        ```python
        parts_list = ["齿轮", "轴承", "螺丝", "马达"]
        for part in parts_list:
            print(f"正在检查零件：{part}")
        ```
    - 遍历字符串：
        ```python
        word = "Python"
        for letter in word:
            print(f"提取出字母：{letter}")
        ```
      - 配合 range() 做固定次数的重复：range(n)会生成0,1,2,3...，n-1这n个数字；range（a,b+1）会生成a,a+1,...b-1,b这b+1-a个数字
        ```python
        for i in range(3):
            print(f"正在进行第 {i} 次测试...")
        ```
6. while循环：只要条件为真，就一直执行
    - 当你不知道要循环多少次，只知道“什么情况下该停下”时，就用 while。
      ```python
        while 条件判断:
            # 只要条件是 True，这里的代码就会一直、反复地执行
      ```
7. 循环控制指令
    - `break`：只要代码碰到了break，程序直接跳出循环体，往下执行。
    - `continue`：遇到 continue，当次循环剩下的代码不执行了，立刻回头跳到循环的最顶端，开始下一轮循环。
    - `pass`：占位符。为什么需要它？ 因为 Python 对语法格式要求极度严格，if 或 while 后面的冒号下方必须有缩进的代码块。如果你在搭程序的骨架，还没想好里面写什么逻辑，为了防止 Python 报错（SyntaxError），就用 pass 占个坑。
8. 循环嵌套
    - 尽量不要超过 3 层嵌套，否则时间复杂度会爆炸。
    - 注意内外层变量名不要混淆。
    - 变量重置位置需正确。
