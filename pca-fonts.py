#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:55:30 2020

@author: alberttenigin
"""


from PIL import Image
from numpy import *
from pylab import *
import pca

im = array(Image.open(imlist[0]))

m, n = im.shape[0:2]

imnum = len(imlist)

immatrix = array([array(Image.open(im)).flatten()
                  for im in imlist], 'f')
V, S, immean = pca.pca(immatrix)

figure()
gray()
subplot(2, 4, 1)
imshow(immean.reshape(m, n))

for i in range(7):
    subplot(2, 4, i+2)
    imshow(V[i].reshape(m, n))
    
show()