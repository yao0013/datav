# -*- coding: utf-8 -*-
# @author ： yao    @Time : 2022/06/09 16:52
import matplotlib.pyplot as plt
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
            edgecolors='none', s=40)
plt.title("xxxxx", fontsize=24)
plt.xlabel("xxxx", fontsize=14)
plt.ylabel("yyyy", fontsize=14)
plt.tick_params(axis="both", which="major", labelsize=14)
plt.axis([0, 1100, 0, 1100000])
# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')

