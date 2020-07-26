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
        
def read_features_from_file(filename):
    """
        reading features from file 'filename'
    """
    f = loadtxt(filename)
    return f[:, :4], f[:, 4:]

def write_features_to_file(filename, locs, desc):
    """
        saving descriptors and locations to file: filename, locations, descriptors
    """

    savetxt(filename, hstack((locs, desc)))
    
def match (desc1, desc2):
    """ 
        Finding each descriptor for both images
    """
    desc1 = array([d/linalg.norm(d) for d in desc1])
    desc2 = array([linalg.norm(d) for d in desc2])
    
    dist_ration = 0.6
    desc1_size = desc1.shape
    matchscores = zeros((desc1_size[0], 1), 'int')
    desc2t = desc2.T
    
    for i in range(desc1_size[0]):
        dotprods = dot(desc1[i, :], desc2t)
        
        dotprods = 0.9999 * dotpods
        
        indx = argsort(arccos(dotpods))
    
        if arccos(dotpods)[indx[0]] < dist_ratio * arccos(dotpods) [indx[1]]:
            matchscores[i] = int(indx[0])
            
    return matchscores