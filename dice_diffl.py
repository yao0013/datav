# -*- coding: utf-8 -*-
# @author ： yao    @Time : 2022/06/13 15:49
import pygal

from die import Die

die1 = Die()
die2 = Die(10)

results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
hist = pygal.Bar()
hist.title = "name of this"
hist.x_labels = list(range(2, 17))
# hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "result"
hist.y_title = "frequency of result"
hist.add('D6*2', frequencies)
hist.render_to_file("die3_v.svg")

# print(frequencies)
