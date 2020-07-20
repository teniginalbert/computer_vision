#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:49:24 2020

@author: alberttenigin
"""

import matplotlib

matplotlib.use('TkAgg')
from PIL import Image
from pylab import *

im = array(Image.open('/home/alberttenigin/Pictures/2.jpg'))
imshow(im)

print('Click 3 times')
x = ginput(n=3, timeout=15, show_clicks=True)
print('You clicked:', x)
first, second, third = x

x1, y1 = first
x2, y2 = second
x3, y3 = third
xs = [x1, x2, x3]
ys = [y1, y2, y3]
plot(xs, ys, 'r*')

show()