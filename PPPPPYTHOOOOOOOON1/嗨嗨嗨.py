# coding=utf-8
# 第一个内容
print("import sys; print('Python %s on %s' % (sys.version, sys.platform))")
print("PyDev console: starting.")
age = int(input("年龄📝:"))
grade = int(input("年级📚:"))
if age >= 8:
    if grade >= 3:
        print("可以参加🎈🎆🎇🧨✨")
    else:
        print("年级不足,Error code:grade not =>3")
        print("不可以参加")
        print("进程即将结束,正在退出代码.......")
        print("进程已结束,退出代码1")
        exit()
else:
    print("年龄不足,Error code:age not =>8")
    print("年级不足,Error code:grade not =>3")
    print("不可以参加")
    print("进程即将结束,正在退出代码.......")
    print("进程已结束,退出代码1")
    exit()
if age >= 8 and grade >= 3:
    print("可以参加🥳")
    print("正在启动游戏......")
else:
    print("不可以参加")
    pass
# 第二个内容
print("Debug started")
import random

print("石头剪刀布😜")
print("石头=1 剪刀✂=2 布=3")
print("输入：")
bot = random.randint(1, 3)
# print("[Debug]bot says >",bot)
play = int(input(">?"))
if bot == 1:
    print("bot出的是:石头")
elif bot == 2:
    print("bot出的是:剪刀✂")
else:
    print("bot出的是:布")
if play == 1 and bot == 2 or play == 2 and bot == 3 or play == 3 and bot == 1:
    print("omg 你赢了🥳")
elif play == bot:
    print("平局")
else:
    print("你死了!!!!")
# 第三个内容
s = 'pythooooon'
for i in s:
    print(i)
# ???
print("还想玩吗?")
try:
    b = input(">?")
    if b == "yes":
        print("石头剪刀布😜")
        while True:
            bot = random.randint(1, 3)
            print("石头=1 剪刀✂=2 布=3")
            print("输入:")
            print("[Debug]bot says >", bot)
            play = int(input(">?"))
            if bot == 1:
                print("bot出的是:石头")
            elif bot == 2:
                print("bot出的是:剪刀✂")
            else:
                print("bot出的是:布")
            if play == 1 and bot == 2 or play == 2 and bot == 3 or play == 3 and bot == 1:
                print("omg 你赢了🥳")
            elif play == bot:
                print("平局😐")
            else:
                print("你死了!!!!")
            if play == 0:
                break
    else:
        pass
except ValueError:
    print("非法字符")
