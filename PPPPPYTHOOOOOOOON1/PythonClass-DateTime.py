# coding=utf-8
credits()


def lesson(python):
    print(f'Hi,{python}')


import datetime
import random
import turtle

turtle.tracer(0)  # 跳过动画
t = turtle.Turtle()
t2 = turtle.Turtle(visible=False)
t3 = turtle.Turtle()
t3.speed(0)
t.speed(0)
t2.speed(0)
t2.pu()
t2.goto(0, -240)
t2.pd()
t2.circle(250)
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

# time返回1970-2262 时间戳_以元组形式存储
# datetime 返回：公元0001年到 公元<em_class:datetime_number:max>    (9999)
now = datetime.datetime.now()


# noinspection PyShadowingNames
def getWeekday(now):  # 取得星期几
    week = ['星期逸', '星期贰', '星期叁', '星期Ⅳ', '星期钨', '星期⑥', '星期囸']
    wd = now.weekday()
    return week[wd]


# noinspection PyShadowingNames
def getTime(now):  # 取得当前时间
    h = now.hour
    m = now.minute
    s = now.second
    return f'{h}时{m}分{s}秒'


# noinspection PyShadowingNames
def getDate(now):  # 取得当前囸器
    y = now.year
    m = now.month
    d = now.day
    return f'{y}年{m}🈷{d}囸'


# noinspection PyShadowingNames
def tick():
    now = datetime.datetime.now()
    t.clear()
    t.write(getDate(now) + getWeekday(now), align='center', font=('微软雅黑', 30, "bold"))
    t.pu()
    t.goto(0, -100)
    t.write(getTime(now), align='center', font=('微软雅黑', 30, "bold"))
    t.goto(0, 0)


def writeDate_on_Turtle():
    tick()
    turtle.ontimer(writeDate_on_Turtle, 1000)


if __name__ == '__main__':
    print(getDate(now))
    print(getTime(now))
    print(getWeekday(now))

turtle.tracer(0)
writeDate_on_Turtle()  # 记时器 在1000
turtle.done()
if __name__ == '__main__':
    print("print done")
