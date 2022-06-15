# -*- coding: utf-8 -*-
# @author ： yao    @Time : 2022/06/15 11:30
import json
import math
import pygal
from itertools import groupby

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list)/len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_char = pygal.Line()
    line_char.title = title
    line_char.x_labels = x_unique
    line_char.add(y_legend, y_mean)
    line_char.render_to_file(title+'.svg')
    return line_char

filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)
dates = []
months = []
weeks = []
weekdays = []
closes = []

for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))
    dates.append(date)
    months.append(month)
    weeks.append(week)
    weekdays.append(weekday)
    closes.append(close)
    # print("{} is month {} week {}, {}, the close price is {} RMB"
    # .format(date, month,week, weekday, close))

print(dates)
print(closes)
line_char = pygal.Line(x_lable_rotation=20, show_minor_x_labels=False)
line_char.title = "收盘价对数变换$"
line_char.x_labels = dates
N = 20
line_char._x_labels_major = dates[::N]
close_log = [math.log10(_) for _ in closes]
line_char.add('shoupanjia', close_log)
line_char.render_to_file('ssgduisu.svg')
