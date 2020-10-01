#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:24:48 2020

@author: alberttenigin
"""


import sys
#import os

sys.path.append('/usr/local/lib64/python3.8/site-packages')

import cv2
import imutils
#import numpy as np
#from numpy import *

face_cascade = cv2.CascadeClassifier("/home/alberttenigin/projects/cv/model_data/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/home/alberttenigin/projects/cv/model_data/haarcascade_eye_tree_eyeglasses.xml")
#eye_cascade = cv2.CascadeClassifier("/home/alberttenigin/projects/cv/model_data/haarcascade_eye.xml")
#eye_cascade = cv2.CascadeClassifier("/home/alberttenigin/projects/cv/model_data/haarcascade_righteye_2splits.xml")


def draw_flow(image):    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (h, w) = gray.shape[:2]
      
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        image = cv2.rectangle(image,(x, y),(x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = image[y : y + h, x : x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey),(ex + ew, ey + eh), (0, 255, 0), 2)
    return image


cap = cv2.VideoCapture('2')
#cap = cv2.VideoCapture('/home/alberttenigin/projects/cv/opencv/sample_cv_1.mp4')
#cap = cv2.VideoCapture('/home/alberttenigin/projects/cv/opencv/blinks_no_eyeglasses.mp4')
cap.open(2)
if not (cap.isOpened()):
    print('Could not open video device')

else:
    while(True):
        ret, im = cap.read()
    
       # im = imutils.rotate(im, -90)
        im = imutils.resize(im, width=500)
        cv2.imshow('Face detection (RT)', draw_flow(im))
    
        if cv2.waitKey(10)== 27:
            break
        
cap.release()

cv2.destroyAllWindows()