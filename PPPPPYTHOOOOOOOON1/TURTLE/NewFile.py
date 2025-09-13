# coding=utf-8
import turtle
t = turtle.Turtle()
t.color("red", "blue")  # turtle.颜色(画笔:"红色",填充:"蓝色")
t.width(10)
t.penup()  # turtle.抬笔🖊
t.goto(-100, -100)  # turtle.去往(x=-100 , y=-100)
t.pendown()  # turtle.落笔🖊
t.begin_fill()  # turtle.开始_填充()
for i in range(8):
    t.forward(100)
    t.left(360 / 8)
t.end_fill()  # turtle.结束_填充()
turtle.done()  # Very important!!!!!! 不关闭海龟窗口
