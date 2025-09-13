# coding=utf-8
# 第一个内容
print("1")
print("只有5行5列星花😕")
for k in range(1, 6):
    for j in range(5):
        print("*", end=" ")
    print("")
print("2")
# 第二个内容
c = input("你要打印社么字符:")
a = int(input("你要打印几行:"))
b = int(input("你要打印几个:"))
for k in range(a):
    print(c * b)
print("3")
# 第叁个内容
for L in range(1, 6):
    print("*" * L)
print("4")
# 第④个内容
for M in range(1, 6):
    d = 5 - M
    print(" " * d, end="")
    print("*" * M)
print("5")
# 第武个内容
for n in range(1, 6):
    d = 5 - n
    f = 2 * n - 1
    print(" " * d, end="")
    print("*" * f)
print("6")
# 第Ⅵ个内容
for o in range(5, 0, -1):
    d = 5 - o
    f = 2 * o - 1
    print(" " * d, end="")
    print("*" * f)
