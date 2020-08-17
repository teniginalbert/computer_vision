#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:20:52 2020

@author: alberttenigin
"""

import sys
import os

sys.path.append('/usr/local/lib64/python3.8/site-packages')

import cv2
import numpy as np
from numpy import *

base_dir = os.path.dirname(__file__)
prototxt_path = os.path.join(base_dir + '/model_data/deploy.prototxt')
caffemodel_path = os.path.join(base_dir + '/model_data/weights.caffemodel')

model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

def draw_flow(image, flow, step=16):    
    vis = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    (h, w) = vis.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(vis, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    
    model.setInput(blob)
    detections = model.forward()
    


           # Create frame around face
    for i in range(0, detections.shape[2]):
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")
        
        confidence = detections[0, 0, i, 2]
      
        # If confidence > 0.5, show box around face
        if (confidence > 0.8):
            cv2.rectangle(vis, (startX, startY), (endX, endY), (0, 0, 255), 2)
     
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
