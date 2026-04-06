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


## 2026.4.2 -“开发环境与基本运行方式”
1. 学会在github上创建仓库，撰写README，提交代码
2. 从官网下载安装python解释器3.12.10
3. 从官网下载安装pycharm2026.1（PS：在网页下载慢，把下载链接复制到迅雷会很快）
4. 打开pycharm，创建自己的第一个项目python_study
5. 在该项目下创建第一个python代码，helloworld

## 2026.4.3 -“变量、数据类型、输入输出”
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
    - 在 Python 中，print() 函数在默认情况下会在末尾自动帮你敲回车。也就是说，当你写下`print("你好")`时，Python 实际上执行的是`print("你好", end="\n")`。
    - end是print函数里的一个特殊参数，它的意思是：“打印完这句话之后，最后要加点什么？”。当你手动写了 end="..." 时，Python 就会听你的，不再偷偷敲回车了。
    - print中可以用+连接字符串
    - print中可以用\转义‘’和“”
    - print“““ ...”””可以让内容自动换行
    - 拼接字符串和变量 `f-string`
    ```python
        name = "小明"
        age = 18
        print(f"我叫{name}，今年{age}岁")
        print("我叫" + name + "，今年" + str(age) + "岁")  # 变量age需要转换成字符串，因为只有字符串才能连接字符串
    ```
8. 输入：`input()`
    - `input()` 得到的是字符串
    - 为什么 input() 默认得到的是字符串？ ——不自作主张，把input进来的所有内容当作纯粹的静态文本对待，保障程序安全和避免用户数据丢失。

## 2026.4.4 -“运算符与条件判断”、“循环：for / while”
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

## 2026.4.6 -“字符串”
1. 字符串是什么？
    - 本质是字符序列，用单引号或双引号表示
2. 字符串的索引，切片[start:end:step]
    ```python
        s = "hello"
        print(s[0])   # 输出h
        print(s[1:4]) # 输出ell
        print(s[::-1])  # 输出olleh（翻转字符串）
    ```
3. 字符串常见操作
    - 拼接 `+`
    - 重复 `*`
    - 成员判断 `in`
    - 长度统计 `len`
4. 字符串常用方法
    - `upper()`：把字符串里的所有英文字母变成大写
    - `lower()`：把字符串里的所有英文字母变成小写
    - `title()`：把字符串里的每个单词首字母大写
        ```python
            part_id = "PaSsEd-woRD"
            print(part_id.upper())  # 输出: PASSED-WORD
            print(part_id.lower())  # 输出: passed-word
            print(part_id.title())  # 输出: Passed-Word
        ```
    - `strip()`：去掉字符串最左边和最右边的空白字符（包括空格、回车符 \n、制表符 \t）；注意，它不管中间的空格。
        ```python
            raw_data = "   1050度   "
            print(raw_data.strip())   # 输出: 1050度  (干净利落)
        ```
    - `replace()`：把字符串里的“旧词”全部换成“新词”。如果把“新词”写成空字符串 ""，就相当于删除操作。
        ```python
            text = "当前压力：1.5MPa，温度：1.5度"
            print(text.replace("1.5", "2.0"))      # 将所有的 1.5 替换成 2.0，输出: 当前压力：2.0MPa，温度：2.0度
            print("1200℃".replace("℃", ""))     # 删除不需要的单位℃，输出: 1200
        ```
    - `split()`：拆分。它像一把刀，按照你指定的“分隔符”（比如逗号、空格、横线），把一长串文字切成好几块，并装进一个列表 (List) 里。如果什么都不填，默认按所有的空白字符切，此时它会自动忽略首尾的空白，自动把中间连续的多个空格当成一个整体切掉。
    - `join()`：缝合。它是 split() 的反操作。用一个你指定的“胶水（字符串）”，把一个列表里的多个元素重新粘合回一长段文字。
        ```python
            sensor_row = "2026-04-06,Sensor_A,1050,Normal"
            data_list = sensor_row.split(",")   # 按照逗号切开
            print(data_list)    # 输出: ['2026-04-06', 'Sensor_A', '1050', 'Normal']

            sensor_row_new = " & ".join(data_list)    # 用 " & " 作为胶水把它们粘起来
            print(sensor_row_new)     # 输出: 2026-04-06 & Sensor_A & 1050 & Normal
        ```
    - `find()`：在文本里寻找某个特定的词。如果找到了，它会告诉你这个词从第几个字符开始出现（索引位置）；如果没找到，它会返回 -1。
    - `count()`：统计某个字或词在整段文字里出现了几次。
    - `startswith()`：判断字符串是不是以某个特定的词开头的，返回布尔值（True 或 False）。
    - `endswith()`：判断字符串是不是以某个特定的词结尾的。
        ```python
            history = "加工开始...重试...温度异常...重试...加工完成"
            print(history.find("重试"))   # 输出: 7
            print(history.count("重试"))  # 输出: 2
            print(history.startswith("重试"))  # 输出:False
            print(history.endswith("加工完成"))  # 输出:True
        ```
5. 格式化输出
    - `f-string`：见2026.4.3 - 7. 输出：print()中的最后一条
    - `format()` ：使用场景为需要先定义好一个带有坑位的“模板”，等程序运行到后面再去填它。
        ```python
            pi = 3.1415926
            ratio = 0.854
            id_num = 7

            print(f"圆周率约等于：{pi:.2f}")
            # 保留两位小数： {:.2f} (f 代表 float 浮点数)
            print("合格率为：{:.1%}".format(ratio))
            # 转为百分比： {:.1%} (保留 1 位小数的百分比)
            print("零件编号：{:0>3}".format(id_num))
            # 用 0 补齐位数： {:0>3} (总共 3 位，不够的在左侧用 0 补齐)
        ```
