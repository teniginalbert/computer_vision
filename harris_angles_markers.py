#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:37:14 2020

@author: alberttenigin
"""


from PIL import Image
from numpy import *
import harris

im = array(Image.open('/home/alberttenigin/Pictures/noisy2.jpg').convert('L'))
harrisim = harris.compute_harris_response(im)
filtered_coords = harris.get_harris_points(harrisim, 6)
harris.plot_harris_points(im, filtered_coords)