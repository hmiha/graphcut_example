#/usr/bin/env python
#-*- coding: utf-8 -*-
# add_noise.py
# 
# usage python add_noise.py <origin> <noise-rate> [<output>]
#

import sys
import random

import Image
from myutil import save_or_show
#import cv2

def add_noise(img_orig, noise_rate):
    width, height = img.size
    S = width * height
    n = int(S * noise_rate + 0.5)

    to_toggle = [False] * S
    for i in range(height): to_toggle[i] = True
    random.shuffle(to_toggle)

    pix = img.load()
    for y in range(height):
        for x in range(width):
            i = y * width + x
            if to_toggle[i]:
                pix[x, y] = 255 - pix[x, y]

    return img
    
def add_noise0(img_orig, noise_rate):
    width, height = img.size
    pix = img.load()
    for y in range(height):
        for x in range(width):
            if random.random() < noise_rate:
                pix[x, y] = 255 - pix[x, y]
    return img

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print "usage: python %s <orig> <noise-rate> [<output>]" % sys.argv[0]
        sys.exit()
    
    infile = sys.argv[1]
    noise_rate = float(sys.argv[2]) / 100
    if len(sys.argv) == 4:
        outfile = sys.argv[3]
    else:
        outfile = None

    img = Image.open(infile)
    img2 = add_noise(img, noise_rate)
    save_or_show(img2, outfile)
    #img2.save("noise.png")

