# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 10:39:51 2023

@author: Jayesh
"""

import cv2 as cv

img = cv.imread('D:\Programming and Development\Image Processing\images/cats and dogs.jpg')

cv.imshow('Original Cat and Dog',img)



def rescaling(img, scale = 0.75):
    weight = int(img.shape[1]*scale)
    height = int(img.shape[0]*scale)
    
    dimensions = (weight,height)
    
    return cv.resize(img , dimensions, interpolation= cv.INTER_AREA)


resized_img = rescaling(img)

cv.imshow('Resized Cat and Dog',resized_img)

cv.waitKey(0)