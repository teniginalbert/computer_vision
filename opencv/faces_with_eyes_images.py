#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:17:41 2020

@author: alberttenigin
"""

import os
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier("/home/alberttenigin/projects/cv/model_data/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("/home/alberttenigin/projects/cv/model_data/haarcascade_eye.xml")

if not os.path.exists('/home/alberttenigin/Pictures/updated_images_with_eyes'):
	print("New directory created")
	os.makedirs('/home/alberttenigin/Pictures/updated_images_with_eyes')
    
#save the image(i) in the same directory
for file in os.listdir('/home/alberttenigin/Pictures/faces/'):
    img = cv2.imread('/home/alberttenigin/Pictures/faces/' + file)  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.imwrite('/home/alberttenigin/Pictures/updated_images_with_eyes/' + file, img)