# -*- coding:utf-8 -*-
__author__ = 'Microcosm'
 
import cv2
import numpy as np
from matplotlib import pyplot as plt
 
img = cv2.imread("a2.jpg")
img2 = img[200:1250,:,:].copy()
template = cv2.imread("template.jpg")
w,h = template.shape[0:2][::-1]
 
# 6 中匹配效果对比算法
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCORR', 'cv2.TM_SQDIFF']
 
for meth in methods:
    img = img2.copy()
 
    method = eval(meth)
 
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
 
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
 
    cv2.rectangle(img,top_left, bottom_right, 0, 2)
 
    print(meth)
    plt.subplot(221), plt.imshow(img2)
    plt.title('Original Image'), plt.xticks([]),plt.yticks([])
    plt.subplot(222), plt.imshow(template)
    plt.title('template Image'),plt.xticks([]),plt.yticks([])
    plt.subplot(223), plt.imshow(res)
    plt.title('Matching Result'), plt.xticks([]),plt.yticks([])
    plt.subplot(224), plt.imshow(img)
    plt.title('Detected Point'),plt.xticks([]),plt.yticks([])
    plt.show()
