#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:33:30 2020

@author: alberttenigin
"""


from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters

im = array(Image.open('/home/alberttenigin/Pictures/1.jpg'))
im2 = array([array(zeros(im.shape)) for i in range(5)])

sigmas = [1, 2, 4, 7, 10]
#plt.figure(figsize=(300, 200))
figure()

subplot(2, 3, 1)
imshow(im)
axis('off')

for image, sigma, k in zip(im2, sigmas, range(5)):
    subplot(2, 3, k + 2)
    for i in range(3):
        image[:, :, i] = filters.gaussian_filter(im[:, :, i], sigma)
    image = uint8(image)
    imshow(image)
    print(k, ' ', sigma)
    axis('off')
    
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 10.5)

show()