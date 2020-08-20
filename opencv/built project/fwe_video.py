#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:24:48 2020

@author: alberttenigin
"""


import sys
import os

sys.path.append('/usr/local/lib64/python3.8/site-packages')

import cv2
import numpy as np
from numpy import *

face_cascade = cv2.CascadeClassifier("/home/alberttenigin/projects/cv/model_data/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/home/alberttenigin/projects/cv/model_data/haarcascade_eye_tree_eyeglasses.xml")

def draw_flow(image, flow, step=16):    
    vis = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    (h, w) = vis.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(vis, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
      
    faces = face_cascade.detectMultiScale(vis, 1.3, 5)
    for (x, y, w, h) in faces:
        img = cv2.rectangle(vis,(x, y),(x + w, y + h), (255, 0, 0), 2)
        roi_gray = vis[y : y + h, x : x + w]
        roi_color = image[y : y + h, x : x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color,(ex, ey),(ex + ew, ey + eh), (0, 255, 0), 2)
    return vis


cap = cv2.VideoCapture('0')
#cap = cv2.VideoCapture('/home/alberttenigin/projects/cv/opencv/sample_5.avi')
cap.open(0)
if not (cap.isOpened()):
    print('Could not open video device')

else:
    while(True):
        ret, im = cap.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

        prev_gray = gray                   
        flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

        cv2.imshow('Face detection (RT)', draw_flow(gray, flow))
    
        if cv2.waitKey(10)== 27:
            break
        
cap.release()

cv2.destroyAllWindows()