#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 16:45:56 2020

@author: alberttenigin
"""
from numpy import *

class KnnClassifier(object):
    
    def __init__(self, labels, samples):
        """
            Initializing with training data
        """
        self.labels = labels
        self.samples = samples
        
    #def L2dist(p1, p2):
    #    return sqrt(sum((p1 - p2) ** 2))
    
    def classify(self, point, k=3):
        """
            Classifying a point by k nearest points of training dataset
        """
        
        dist = array([(sqrt(sum((point - s) ** 2))) for s in self.samples])
        
        ndx = dist.argsort()
        
        votes = {}
        for i in range(k):
            label = self.labels[ndx[i]]
            votes.setdefault(label, 0)
            votes[label] += 1
            
        return max(votes)
    
    # def L2dist(p1, p2):
    #     return sqrt(sum((p1 - p2) ** 2))