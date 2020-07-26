#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:20:15 2020

@author: alberttenigin
"""

from numpy import *
import knn

import os, sift

def read_gesture_features_labels(path):
    """
        creating list of all files with .dsift format
    """
    featlist = [os.path.join(path, f) for f in os.listdir(path) \
                if f.endswith('.dsift')]
    features = []
    
    for featfile in featlist:
        l, d = sift.read_features_from_file(featfile)
        features.append(d.flatten())
        
    features = array(features)
    
    labels = [featfile.split('/')[-1][0] for featfile in featlist]
    
    return features, array(labels)

test_path = '/home/alberttenigin/projects/cv/classifiers/gestures_test/'
train_path ='/home/alberttenigin/projects/cv/classifiers/gestures_training/'

features, labels = read_gesture_features_labels(train_path)

test_features, test_labels = read_gesture_features_labels(test_path)

classnames = unique(labels)

k = 1

knn_classifier = knn.KnnClassifier(labels, features)
res = array([knn_classifier.classify(test_features[i], k)\
            for i in range(len(test_labels))])
    
accuracy = sum(1.0 * (res == test_labels)) / len(test_labels)
print('Accuracy is: ', accuracy)
print('Classnames \n', classnames)
print('Test labels of len ', len(test_labels), ' are ', test_labels)
print('Test features are: \n', test_features)
print('\nTrain features are\n:', features)
