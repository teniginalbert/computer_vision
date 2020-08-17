#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:26:08 2020

@author: alberttenigin
"""


import os
import cv2
import numpy as np

base_dir = os.path.dirname(__file__)
prototxt_path = os.path.join(base_dir + '/model_data/deploy.prototxt')
caffemodel_path = os.path.join(base_dir + '/model_data/weights.caffemodel')

model = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

if not os.path.exists('/home/alberttenigin/Pictures/updated_images'):
	print("New directory created")
	os.makedirs('/home/alberttenigin/Pictures/updated_images')
    
for file in os.listdir('/home/alberttenigin/Pictures/faces/'):
    file_name, file_extension = os.path.splitext(file)
    if (file_extension in ['.png','.jpg']):
        print("Image path: {}".format('/home/alberttenigin/Pictures/faces/' + file))
    
        image = cv2.imread('/home/alberttenigin/Pictures/faces/' + file)

        (h, w) = image.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))

        model.setInput(blob)
        detections = model.forward()
    
        # Create frame around face
        for i in range(0, detections.shape[2]):
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            confidence = detections[0, 0, i, 2]
      
            # If confidence > 0.5, show box around face
            if (confidence > 0.9):
                cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)

        cv2.imwrite('/home/alberttenigin/Pictures/updated_images/' + file, image)
        print("Image " + file + " converted successfully")