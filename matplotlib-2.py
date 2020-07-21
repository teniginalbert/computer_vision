#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:39:59 2020

@author: alberttenigin
"""


from PIL import Image
from pylab import *

im = array(Image.open('/home/alberttenigin/Pictures/2.jpg').\
           convert('L'))
figure()

#hist(im.flatten(),128) 

gray()

#iso

contour(im, origin='image')
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(10.5, 16.5)
axis('equal')
axis('off')