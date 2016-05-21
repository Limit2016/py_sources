# -*- coding: utf-8 -*-

# pi.py

from random import random
from math import sqrt
from time import clock

DARTS = input() 
hits = 0
clock()
i=0

while i<=DARTS :
    x, y = random(), random()
    dist = sqrt(x**2 + y**2)

    if dist <= 1.0:
        hits = hits + 1

    i+=1


pi = 4 * (float(hits)/DARTS)
print("Pi的值是 %s" % pi)
print("程序运行时间是 %-5.5ss" % clock())
