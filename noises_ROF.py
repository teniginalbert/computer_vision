#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:16:51 2020

@author: alberttenigin
"""

from PIL import Image
from numpy import *
from pylab import *
from numpy import random
from scipy.ndimage import filters
import rof

#im = zeros((500, 500))

#im[100:400, 100:400] = 128
#im[200:300, 200:300] = 255
#im = im + 30 * random.standard_normal((500, 500))

im = array(Image.open('/home/alberttenigin/Pictures/noisy2.jpg').convert('L'))

print(im.shape)

U, T = rof.denoise(im, im)
G = filters.gaussian_filter(im, 10)

images = [im, U, G]

figure()
for image, i in zip(images, range(3)):
    subplot(1, 3, i + 1)
    imshow(image)
    axis('off')
  
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 10.5)
show()