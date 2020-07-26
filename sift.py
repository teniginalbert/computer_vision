#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 19:43:43 2020

@author: alberttenigin
"""
from PIL import Image
from pylab import *

def process_image(imagename, resultname, params="--edge-thresh 10 --peak-thresh 5"):
    if imagename[-3:] != 'pgm':
        im = Image.open(imagename).convert('L')
        im.save('tmp.pgm')
        imagename = 'tmp.pgm'
        
        cmmd = str("sift " + imagename + " --output=" + resultname + " " + params)
        os.system(cmmd)
        print('Processed ', imagename, ' to ', resultname)