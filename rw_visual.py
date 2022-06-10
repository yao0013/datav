# -*- coding: utf-8 -*-
# @author ： yao    @Time : 2022/06/10 16:21
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    # plt.figure(figsize=(10, 6 ))
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_value, rw.y_value, linewidth=1)
    # plt.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues,
    #             edgecolor='none', s=1)
    # plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    # plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none',
    #             s=100)
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    plt.axis('off')
    plt.show()
    keep_running = input("are you go on?(y/n)")
    if keep_running == 'n':
        break
