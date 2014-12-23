#/usr/bin/env python
#-*- coding: utf-8 -*-
# add_noise.py
# 
# usage python add_noise.py <origin> <noise-rate> [<output>]
#

import sys
import random

#import Image
from myutil import save_or_show
import cv2
import numpy as np
   
def add_noise0(img, noise_rate):
    height, width = img.shape
    
    for y in range(height):
        for x in range(width):
            if random.random() < noise_rate:
                img[x, y] = abs(255 - img[x, y])
    return img

def bin(img):

    mask = img > 122
    im_bi = np.zeros((img.shape[0],img.shape[1]),np.uint8)
    im_bi[mask] = 255
    return im_bi

if __name__ == "__main__":

    infile = "img.jpg"

    noise_rate = float(sys.argv[1]) / 100
    #noise_rate = 5.0 / 100
    img = cv2.imread(infile, 0)
    img = bin(img)
    img2 = add_noise0(img, noise_rate)
    cv2.imwrite("noise.png", img2)

