# -*- coding: utf-8 -*-
"""
Created on Sat May 26 19:37:00 2018

@author: Nilansh
"""

import numpy as np
import cv2

im = cv2.imread('download.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
#image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('cont',thresh)