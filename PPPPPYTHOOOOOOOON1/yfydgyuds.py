# coding=utf-8
import random
# 第一个内容
a = random.randint(1, 10)  # a=1-10之间随机数
b = random.randint(3, 16)  # b=3-16之间随机数
c = random.randint(4, 17)  # c=4-17之间随机数
print(a, b, c)
# 第二个内容
print("1-10 猜数字🐱‍💻")
d = 0  # d=0 空变量
while a != d:
    d = input("数字:")
    d = int(d)  # d = 整数(d)  d为整数
    if a < d:  # 如果a(随机数)<d(输入的数字)
        print("太大🤔")
    elif a > d:
        print("太小🤔")
    else:
        print("完美🥳🎉")
# 第三个内容
# 注意,已使用a,b,c,d!!!!!!
e = int(input("语文成绩📝:"))  # e=整数(输入(语文成绩📝:))
f = int(input("数学成绩📝:"))
if e == 100 or f == 100:  # 如果e=100
    print("OKAY,you can go!🥳🎉🎆🎇🥳")
else:
    print("GET OUT OF THERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!🤬🤬😡😡🤬")
# 第四个内容
# 注意,已使用a,b,c,e,f!!!!
g = input("颜色:")
if g == "green" or g == "blue" or g == "red":
    print("OKAY,you can go")
else:
    print("GEO OUT WHILE YOU STILL YOU CAN!!!!!!!!!🤬🤬🤬🤬")
    print("hen hen hen......")
