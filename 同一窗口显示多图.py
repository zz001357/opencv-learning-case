# -*- coding: utf-8 -*-
# @File:同一窗口显示多图.py
# @Author: Zhang Ze
# @Date:   2024-08-18
# @Last Modified by:   Zhang Ze

import matplotlib.pyplot as plt
import cv2
import numpy as np
import pyautogui

img1 = cv2.imread('./img/_DSF0501-1.jpg')
img2 = cv2.imread('./img/_DSF0488-1.jpg')
img3 = cv2.imread('./img/_DSF1297_gray.jpg')

img_list = [img1, img2, img3]


for i, img in enumerate(img_list):
    # 调换RGB通道顺序，改变原图颜色失真
    b, g, r = cv2.split(img)
    img = cv2.merge([r, g, b])

    title = "title" + str(i + 1)
    # 行，列，索引(这里设置为一行3个)
    plt.subplot(3, 3, i + 1)
    plt.imshow(img)
    plt.title(title, fontsize=8)
    plt.xticks([])
    plt.yticks([])
plt.show()

