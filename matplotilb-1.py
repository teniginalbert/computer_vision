#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 12:36:55 2020

@author: alberttenigin
"""


from PIL import Image
from pylab import *

im = array(Image.open('/home/alberttenigin/Pictures/Wallpapers/118509.jpg'))

imshow(im)

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

plot(x, y) #default blue line
plot(x, y, 'ks:') #black dotted line, square points
plot(x, y, 'go-') #green line, circle points
plot(x, y, 'r*') #red stars
"""
'b' blue
'g' green
'r' red
'c' cyan
'm' purple
'y' yellow
'k' black
'w' white

'-'
'--'
':'

'.'
'o'
's'
'*'
'+'
'x'
"""
plot(x[:2], y[:2])

title('Plotting: "/home/alberttenigin/Pictures/Wallpapers/118509.jpg"')

show()
