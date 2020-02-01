# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 11:40:43 2020

@author: CEC
"""

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(300)
    left(200)
    if abs(pos()) < 1:
        break
end_fill()
done()

