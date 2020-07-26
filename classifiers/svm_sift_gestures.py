#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 23:00:59 2020

@author: alberttenigin
"""

import os, sys, sift
from numpy import *

sys.path.append('/home/alberttenigin/Downloads/libsvm-3.24/python')
from svmutil import *

def convert_labels(labels, transl):
    """
        Convert between strings and numbers
    """
    return [transl[i] for i in labels]

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
#features = map(list, features)
#test_features = map(list, test_features)

transl = {}

for i, c in enumerate(classnames):
    transl[c], transl[i] = i, c
    
prob = svm_problem(convert_labels(labels, transl), features)
param = svm_parameter('-t 2')

m = svm_train(prob, param)

#res = svm_predict(convert_labels(labels, transl), features, m)

res = svm_predict(convert_labels(test_labels, transl), test_features, m)[0]
res = convert_labels(res, transl)

accuracy = sum(1.0 * (res == test_labels)) / len(test_labels)
print('Accuracy is: ', accuracy)
print('Classnames \n', classnames)
print('Test features are: \n', test_features)