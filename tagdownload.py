#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 16:36:29 2020

@author: alberttenigin
"""


import flickr_api
flickr_api.set_keys(api_key = 'a796ceabadd1ea809344775fdf9f1bf4',\
                    api_secret = '5b97e15f19d1ff60')
    
import urllib
import os
import sys

if len(sys.argv) > 1:
    tag = sys.argv[1]
else:
    print('label not specified')
    
f = flickr_api #photos_search(tags=tag)
urllist = []

for k in f:
    url = k.getURL(size='Medium', urlType='Source')
    urllist.append(url)
    image = urllib.URLopener()
    image.retrieve(url, os.path.basename(urllib.parse.urlparse(url).path))
    print('downloading ', url)