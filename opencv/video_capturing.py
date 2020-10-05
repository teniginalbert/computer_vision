#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 01:17:39 2020

@author: alberttenigin
"""

import sys

sys.path.append('/usr/local/lib64/python3.8/site-packages')

import cv2
import numpy
from numpy import *

def draw_flow(im, flow, step=16):
    h, w = im.shape[:2]
    y, x = mgrid[step / 2 : h : step, step / 2 : w : step].reshape(2, -1)
    y = array(y, dtype = numpy.int64)
    x = array(x, dtype = numpy.int64)
    fx, fy = flow[y, x].T
    
    lines = vstack([x, y, x + fx, y + fy]).T.reshape(-1, 2, 2)
    lines = lines
    lines = int64(lines)
    
    vis = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
    for(x1, y1), (x2, y2) in lines:
        cv2.line(vis, (x1, y1), (x2 + (x2 - x1) * 2, y2 + (y2 - y1) * 2), (0, 255, 0), 1)
        cv2.circle(vis, (x1, y1), 1, (0, 255, 0), -1)
        
    return vis


cap = cv2.VideoCapture('3')
#cap = cv2.VideoCapture('/home/alberttenigin/projects/cv/opencv/sample_5.avi')
cap.open(3)
if not (cap.isOpened()):
    print('Could not open video device')

else:
    while(True):
        ret, im = cap.read()
        #gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        #prev_gray = gray                   
        #flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        cv2.imshow('Optical flow', im)
    
        if cv2.waitKey(10)== 27:
            break
        
cap.release()

cv2.destroyAllWindows()