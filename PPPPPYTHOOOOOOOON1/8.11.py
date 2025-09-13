# coding=utf-8
def python_lesson(turtlet):
    print(f'Hi,{turtlet}')


def coopyright():
    print("Copyright (c) 2010-2025 Comic Python 6405 Foundation.\nAll Rights Reserved.\n")


if __name__ == '__main__':
    coopyright()

# #############{分隔符}#####################
# ==============={准备工作}=============
import turtle
import random

turtle_screen = turtle.Screen()
a = random.random()
b = random.randint(1, 2)
t1 = turtle.Turtle()

# --------------------------
turtle_screen.setup(800, 600)
turtle_screen.bgcolor("DodgerBlue")

# ----------------
colors = ['pink', 'black', 'white', 'blue', 'cyan', 'yellow']
y = [250, 150, 50, -50, -150, -250]
all_turtle = []
for i in range(6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.speed(0)
    new_turtle.color(colors[i])
    new_turtle.pu()
    new_turtle.goto(-500, y[i])
    all_turtle.append(new_turtle)
    new_turtle.speed(a)
t1.speed(0)
t1.pu()
t1.goto(-450, 300)
t1.pd()
t1.right(90)
t1.forward(600)
t1.left(90)
t1.pu()
t1.goto(450, 300)
t1.pd()
t1.right(90)
t1.forward(600)
t1.left(90)
t1.pu()
t1.goto(-10, 300)
t1.pd()

"""def Crash():
    立刻马上给我崩溃
"""

# --------------
race = True
cai = turtle_screen.textinput("Turtle Race", "Choose Your Color")
while race:
    for Turtle in all_turtle:
        if Turtle.xcor() > 450:
            race = False
            win_color = Turtle.pencolor()
            if win_color == cai:
                print(f"恭喜，你赢了")
            else:
                print(f"LLLLLLLLLL,你输了😂😂😂🤣🤣🤣🤣,{win_color}")

        x = random.randint(1, 10)
        Turtle.forward(x)

    # ###############{分隔符}####################
# ============[创建函数]=================


# #############{分隔符}######################
# ==========={诸臣是}===================

print('Done')
turtle.done()
