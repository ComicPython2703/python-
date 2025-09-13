# coding=utf-8
# Title = 模拟时钟
import random


# noinspection PyPep8Naming
def Copyright():
    print("'Copyright (c) 2010-2024 Comic Python 6405 Foundation.\nAll Rights Reserved.\n")


if __name__ == '__main__':
    Copyright()
    print()
    print()


def lesson(python):
    print(f'Hi,{python}')


# ============={准备工作}================
# noinspection PyPep8
import datetime
import turtle
now = datetime.datetime.now()
t1 = turtle.Turtle(visible=False)
t2 = turtle.Turtle(visible=False)
t3 = turtle.Turtle(visible=False)
t4 = turtle.Turtle(visible=False)
turtle.tracer(0)  # 跳过动画
t1.pu()
t1.goto(0, -220)
t1.pd()
t1.circle(220)
t1.pu()
t1.goto(0, 0)
t1.pd()
for i in range(100):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    c = random.random()
    c1 = random.random()
    c2 = random.random()
    t3.pu()
    t3.goto(x, y)
    t3.pd()
    t3.color(c, c1, c2)
    t3.circle(20)


# =============={分隔符}===============
# ##############{创建函数}##################
# noinspection PyShadowingNames,PyPep8Naming
def getWeekday(now):  # 取得星期几
    week = ['星期逸', '星期贰', '星期叁', '星期Ⅳ', '星期钨', '星期⑥', '星期囸']
    wd = now.weekday()
    return week[wd]


# noinspection PyShadowingNames,PyPep8Naming
def getTime(now):  # 取得当前时间
    h = now.hour
    m = now.minute
    s = now.second
    return f'{h}时{m}分{s}秒'


# noinspection PyShadowingNames,PyPep8Naming
def getDate(now):  # 取得当前囸器
    y = now.year
    m = now.month
    d = now.day
    return f'{y}年{m}🈷{d}囸'


def move(n):
    t1.pu()
    t1.forward(n)
    t1.pd()


# noinspection PyShadowingNames
def clock_pan():
    t1.pensize(6)
    for i in range(60):
        move(200)
        if i % 5 == 0:
            t1.forward(10)
            t1.pu()
            t1.goto(0, 0)
        else:
            t1.dot(10)
            t1.pu()
            t1.goto(0, 0)
        t1.left(6)


# noinspection PyShadowingNames
def time_clock():
    now = datetime.datetime.now()
    h = now.hour
    m = now.minute
    s = now.second
    t2.clear()
    # 时针
    t2.seth(90)  # 🖊2.绝对方向(90)
    t2.right(h * 30 + m * 0.5)
    t2.width(5)
    t2.fd(100)
    t2.bk(100)
    # 分针
    t2.seth(90)
    t2.right(m * 6 + s * 0.1)
    t2.width(3)
    t2.fd(150)
    t2.bk(150)
    # 秒针
    t2.seth(90)
    t2.right(s * 6)
    t2.width(2)
    t2.fd(140)
    t2.bk(140)


def tick_for_clock():
    time_clock()
    turtle.update()
    turtle.ontimer(tick_for_clock, 1000)


# noinspection PyShadowingNames
def tick():
    now = datetime.datetime.now()
    t4.clear()
    t4.write(getDate(now) + getWeekday(now), align='center', font=('微软雅黑', 30, "bold"))
    t4.pu()
    t4.goto(0, -100)
    t4.write(getTime(now), align='center', font=('微软雅黑', 30, "bold"))
    t4.goto(0, 0)


# noinspection PyPep8Naming
def writeDate_on_Turtle():
    tick()
    turtle.ontimer(writeDate_on_Turtle, 1000)


# ==========={分隔符}===================
# ###############{程式}#####################\
clock_pan()
tick_for_clock()
writeDate_on_Turtle()
if __name__ == '__main__':
    print("done")

turtle.done()
