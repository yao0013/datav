# -*- coding: utf-8 -*-
# @author ： yao    @Time : 2022/06/13 15:49
import pygal

from die import Die

die = Die()
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
hist = pygal.Bar()
hist.title = "name of this"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "result"
hist.y_title = "frequency of result"
hist.add('D6', frequencies)
hist.render_to_file("die_v.svg")

# print(frequencies)
