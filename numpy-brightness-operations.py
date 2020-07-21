#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:26:38 2020

@author: alberttenigin
"""


from PIL import Image
from pylab import *

im = array(Image.open('/home/alberttenigin/Pictures/2.jpg').convert('L'))
im2 = 255 - im
im3 = (100.0/255) * im + 100
im4 = 255.0 * (im/255.0) ** 2

print('im', int(im.min()), int(im.max()))
print('im2', int(im2.min()), int(im2.max()))
print('im3', int(im3.min()), int(im3.max()))
print('im4', int(im4.min()), int(im4.max()))

imshow(im4)