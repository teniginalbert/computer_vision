#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:39:59 2020

@author: alberttenigin
"""


from PIL import Image
from pylab import *

im = array(Image.open('/home/alberttenigin/Pictures/3.jpg').\
           convert('L'))
figure()

#hist(im.flatten(),128) 

gray()

#iso

contour(im, origin='image')
axis('equal')
axis('off')