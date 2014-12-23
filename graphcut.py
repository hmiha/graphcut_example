#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
 
from myutil import save_or_show
import cv2
import numpy
 
from graph_tool.all import *
 
def remove_noise(img):
    height, width = img.shape

    # 面積
    S = width * height
 
    # グラフ生成
    g = Graph()
    capacity = g.new_edge_property("int")
 
    for i in range(S):
        v = g.add_vertex()

    start = g.add_vertex()
    goal = g.add_vertex()
 
    pix = img
 
    for x in range(width):
        for y in range(height):
            i = y*width + x
            # 各ピクセルにラベル付与
            p = 1 if pix[x,y] == 255 else 0  # {0, 1}
 
            e = g.add_edge(start, i)
            capacity[e] = 5 + 4*p
 
            e = g.add_edge(i, goal)
            capacity[e] = 5 + 4*(1-p)
 
    for i in range(S):
        if i > 0:
            e = g.add_edge(i, i-1)
            capacity[e] = 3
        if i < S-1:
            e = g.add_edge(i, i+1)
            capacity[e] = 3
        if i >= width:
            e = g.add_edge(i, i-width)
            capacity[e] = 3
        if i < S-width:
            e = g.add_edge(i, i+width)
            capacity[e] = 3
 
    residual = push_relabel_max_flow(g, start, goal, capacity)
    partition = min_st_cut(g, start, capacity, residual)
 
    for i in range(S):
        x = i % width
        y = i / width
        pix[x,y] = 255 if partition.a[i] else 0
 
    return img
 
 
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage: python %s <input> [<output>]" % sys.argv[0]
        sys.exit()

    infile = sys.argv[1]
    #img = Image.open(infile)
    img = cv2.imread(infile, 0)

    img2 = remove_noise(img)
    cv2.imwrite("denoise.png", img2)
