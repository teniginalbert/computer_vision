#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:17:50 2020

@author: alberttenigin
"""


from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters

im = array(Image.open('/home/alberttenigin/Pictures/1.jpg'))

imx = zeros(im.shape)
filters.sobel(im, 1, imx)

imy = zeros(im.shape)
filters.sobel(im, 0, imy)

magnitude = sqrt(imx ** 2 + imy ** 2)


