#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:04:30 2020

@author: alberttenigin
"""

#lines 10-34 are from pca-fonts.py

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

f = open('font_pca_modes.pkl', 'wb')
pickle.dump(immean, f)
pickle.dump(V, f)
f.close()


#for loading
"""
immean = pickle.load(f)
V = pickle.load(f)
"""