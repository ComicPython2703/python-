# coding=utf-8
import datetime
now = datetime.datetime.now()
# noinspection PyShadowingNames
def getWeekday():  # 取得星期几
    week = ['星期逸', '星期贰', '星期叁', '星期Ⅳ', '星期钨', '星期⑥', '星期囸']
    wd = now.weekday()
    return week[wd]


# noinspection PyShadowingNames
def getTime():  # 取得当前时间
    h = now.hour
    m = now.minute
    s = now.second
    return f'{h}时{m}分{s}秒'


# noinspection PyShadowingNames
def getDate():  # 取得当前囸器
    y = now.year
    m = now.month
    d = now.day
    return f'{y}年{m}🈷{d}囸'



