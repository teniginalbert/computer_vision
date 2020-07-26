#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:24:14 2020

@author: alberttenigin
"""

from numpy import *
from numpy.random import randn
import pickle

n = 200

class_1 = 0.6 * randn(n, 2)
class_2 = 1.2 * randn(n, 2) + array([5, 1])
labels = hstack((ones(n), -ones(n)))

#class_1 = array_str(class_1)
#class_2 = array_str(class_2)
#labels = array_str(labels)

with open('points_normal_test.pkl', 'wb') as f:
    pickle.dump(class_1, f)
    pickle.dump(class_2, f)
    pickle.dump(labels, f)
    
class_1 = 0.6 * randn(n, 2)
r = 0.8 * randn(n, 1) + 5
angle = 2 * pi * randn(n, 1)
class_2 = hstack((r * cos(angle), r* sin(angle)))
labels = hstack((ones(n), -ones(n)))

with open('points_ring_test.pkl', 'wb') as f:
    pickle.dump(class_1, f)
    pickle.dump(class_2, f)
    pickle.dump(labels, f)