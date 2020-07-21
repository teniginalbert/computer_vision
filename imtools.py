#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:34:26 2020

@author: alberttenigin
"""

from PIL import Image
from pylab import *

"""
resize the image to sz
"""
def imresize(im,sz):
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))

"""
flattening hist of half-tone image
"""
def histeq(im, nbr_bins=256):
    
    imhist, bins = histogram(im.flatten(), nbr_bins, normed=True)
    
    cdf = imhist.cumsum()
    cdf = 255 * cdf / cdf[-1]
    
    im2 = interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf

"""
computing the average of image list
"""
def compute_average(imlist):
    averageim = array(Image.open(imlist[0], 'f'))
    
    for imname in imlist[1:]:
        try:
            averageim += array(Image.open(imname))
        except:
            print(imname + '... was skipped')
            averageim /= len(imlist)
            
    return array(averageim, 'uint8')