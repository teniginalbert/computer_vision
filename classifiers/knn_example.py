#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:31:23 2020

@author: alberttenigin
"""


from numpy import *
import pickle 
import knn
import imtools

with open('points_normal.pkl', 'rb') as f:
    class_1 = pickle.load(f)
    class_2 = pickle.load(f)
    labels = pickle.load(f)
    model = knn.KnnClassifier(labels, vstack((class_1, class_2)))
    
with open('points_normal_test.pkl', 'rb') as  f:
    class_1 = pickle.load(f)
    class_2 = pickle.load(f)
    labels = pickle.load(f)
    
print(model.classify(class_1[0]))