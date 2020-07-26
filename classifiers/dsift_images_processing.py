#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 19:54:42 2020

@author: alberttenigin
"""

import dsift

imlist_a = []
imlist_b = []
imlist_c = []
imlist_f = []
imlist_v = []
imlist_p = []

path = '/home/alberttenigin/projects/cv/classifiers/gestures_training/'

for i in range(1,10):
    imlist_a.append(path + 'A-train000' + str(i) + '.ppm')
for i in range(10,100):
    imlist_a.append(path + 'A-train00'  + str(i) + '.ppm')
for i in range(100,1000):
    imlist_a.append(path + 'A-train0'   + str(i) + '.ppm')
for i in range(1000,1330):
    imlist_a.append(path + 'A-train'    + str(i) + '.ppm')
    
for i in range(1,10):
    imlist_b.append(path + 'B-train00' + str(i) + '.ppm')
for i in range(10,100):
    imlist_b.append(path + 'B-train0'  + str(i) + '.ppm')
for i in range(100,488):
    imlist_b.append(path + 'B-train'   + str(i) + '.ppm')
    
for i in range(1,10):
    imlist_c.append(path + 'C-train00' + str(i) + '.ppm')
for i in range(10,100):
    imlist_c.append(path + 'C-train0'  + str(i) + '.ppm')
for i in range(100,573):
    imlist_c.append(path + 'C-train'   + str(i) + '.ppm')  
    
for i in range(1,10):
    imlist_f.append(path + 'Five-train00' + str(i) + '.ppm')
for i in range(10,100):
    imlist_f.append(path + 'Five-train0'  + str(i) + '.ppm')
for i in range(100,654):
    imlist_f.append(path + 'Five-train'   + str(i) + '.ppm')
    
for i in range(1,10):
    imlist_p.append(path + 'Point-train000' + str(i) + '.ppm')
for i in range(10,100):
    imlist_p.append(path + 'Point-train00'  + str(i) + '.ppm')
for i in range(100,1000):
    imlist_p.append(path + 'Point-train0'   + str(i) + '.ppm')
for i in range(1000,1396):
    imlist_p.append(path + 'Point-train'    + str(i) + '.ppm')
    
for i in range(1,10):
    imlist_v.append(path + 'V-train00' + str(i) + '.ppm')
for i in range(10,100):
    imlist_v.append(path + 'V-train0'  + str(i) + '.ppm')
for i in range(100,436):
    imlist_v.append(path + 'V-train'   + str(i) + '.ppm')

for filename in imlist_a:
    featfile = filename[:-3] + 'dsift'
    dsift.process_image_dsift(filename, featfile, 10, 5, resize=(50, 50))

for filename in imlist_b:
    featfile = filename[:-3] + 'dsift'
    dsift.process_image_dsift(filename, featfile, 10, 5, resize=(50, 50))

for filename in imlist_c:
    featfile = filename[:-3] + 'dsift'
    dsift.process_image_dsift(filename, featfile, 10, 5, resize=(50, 50))

for filename in imlist_f:
    featfile = filename[:-3] + 'dsift'
    dsift.process_image_dsift(filename, featfile, 10, 5, resize=(50, 50))

for filename in imlist_p:
    featfile = filename[:-3] + 'dsift'
    dsift.process_image_dsift(filename, featfile, 10, 5, resize=(50, 50))

for filename in imlist_v:
    featfile = filename[:-3] + 'dsift'
    dsift.process_image_dsift(filename, featfile, 10, 5, resize=(50, 50))
    