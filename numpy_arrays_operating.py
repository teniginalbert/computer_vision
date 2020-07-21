#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:17:45 2020

@author: alberttenigin
"""


from PIL import Image
from pylab import *

im = array(Image.open('/home/alberttenigin/Pictures/2.jpg'))
print(im.shape, im.dtype)

im = array(Image.open('/home/alberttenigin/Pictures/2.jpg').convert('L'), 'f')
print(im.shape, im.dtype) 

im[i,:] = im[j,:] #copy values from j to i
im[:,i] = 100 #all values of i are 100 now
im[:100, :50].sum() #sum all values in first 0-100, 0-50
im[50:100, 50:100]
im[i].mean() #mean value of i
im[-2, :]