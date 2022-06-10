# -*- coding: utf-8 -*-
# @author ： yao    @Time : 2022/06/09 15:52
import matplotlib.pyplot as plt
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)
plt.title("Numbers", fontsize=24)
plt.xlabel("value", fontsize=14)
plt.ylabel("Square", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()
