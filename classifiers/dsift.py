#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 19:32:48 2020

@author: alberttenigin
"""
from pylab import *
from numpy import *
from PIL import Image
import sift
import os

def process_image_dsift(imagename, resultname, size=20, steps=10,\
                        force_orientation=False, resize=None):
    im = Image.open(imagename).convert('L')
    if resize != None:
        im = im.resize(resize)
    m, n = im.size
    
    if imagename[-3:] != 'pgm':
        im.save('tmp.pgm')
        imagename = 'tmp.pgm'
        
    scale = size / 3.0
    x, y = meshgrid(range(steps, m, steps), range(steps, n, steps))
    xx, yy = x.flatten(), y.flatten()
    
    frame = array([xx, yy, scale * ones(xx.shape[0]), zeros(xx.shape[0])])
    savetxt('tmp.frame', frame.T, fmt='%03.3f')
    
    if force_orientation:
        cmmd = str("sift " + imagename + " --output=" + resultname + \
                   " --read-frames=tmp.frame --orientations")
    else:
        cmmd = str("sift " + imagename + " --output=" + resultname + \
                   " --read-frames=tmp.frame")
            
    os.system(cmmd)
    print('Processed ', imagename, ' to ', resultname)