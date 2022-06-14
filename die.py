# -*- coding: utf-8 -*-
# @author ： yao    @Time : 2022/06/13 15:37
from random import randint


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
