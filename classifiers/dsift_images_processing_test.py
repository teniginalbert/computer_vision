#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:08:57 2020

@author: alberttenigin
"""

import dsift

imlist_a = []
imlist_b = []
imlist_c = []
imlist_f = []
imlist_v = []
imlist_p = []

path = '/home/alberttenigin/projects/cv/classifiers/gestures_test/'

for i in range(1,10):
    imlist_a.append(path + 'A-uniform0' + str(i) + '.ppm')
for i in range(10,59):
    imlist_a.append(path + 'A-uniform'  + str(i) + '.ppm')

for i in range(1,10):
    imlist_b.append(path + 'B-uniform0' + str(i) + '.ppm')
for i in range(10,62):
    imlist_b.append(path + 'B-uniform'  + str(i) + '.ppm')

for i in range(1,10):
    imlist_c.append(path + 'C-uniform0' + str(i) + '.ppm')
for i in range(10,66):
    imlist_c.append(path + 'C-uniform'  + str(i) + '.ppm')
 
for i in range(1,10):
    imlist_f.append(path + 'Five-uniform0' + str(i) + '.ppm')
for i in range(10,77):
    imlist_f.append(path + 'Five-uniform'  + str(i) + '.ppm')

for i in range(1,10):
    imlist_p.append(path + 'Point-uniform0' + str(i) + '.ppm')
for i in range(10,66):
    imlist_p.append(path + 'Point-uniform'  + str(i) + '.ppm')

for i in range(1,10):
    imlist_v.append(path + 'V-uniform0' + str(i) + '.ppm')
for i in range(10,58):
    imlist_v.append(path + 'V-uniform'  + str(i) + '.ppm')

for filename in imlist_a:
    featfile = filename[:-3] + 'dsift'
    dsift.process_image_dsift(filename, featfile, 5, 2, resize=(50, 50))

for filename in imlist_b:
    featfile = filename[:-3] + 'dsift'
    dsift.process_image_dsift(filename, featfile, 5, 2, resize=(50, 50))

for filename in imlist_c:
    featfile = filename[:-3] + 'dsift'
    dsift.process_image_dsift(filename, featfile, 5, 2, resize=(50, 50))

for filename in imlist_f:
    featfile = filename[:-3] + 'dsift'
    dsift.process_image_dsift(filename, featfile, 5, 2, resize=(50, 50))

for filename in imlist_p:
    featfile = filename[:-3] + 'dsift'
    dsift.process_image_dsift(filename, featfile, 5, 2, resize=(50, 50))

for filename in imlist_v:
    featfile = filename[:-3] + 'dsift'
    dsift.process_image_dsift(filename, featfile, 5, 2, resize=(50, 50))
    