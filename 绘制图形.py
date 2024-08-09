# -*- coding: utf-8 -*-
# @File:绘制图形.py
# @Author: Zhang Ze
# @Date:   2024-07-22
# @Last Modified by:   Zhang Ze


# 1.导入cv模块
import cv2

# 2.导入图片
img = cv2.imread('./img/_DSF1297.jpg')

# 3.绘制图像
x, y, z, h = 100, 100, 100, 100

# 3.1.绘制矩形(图像，（起始点x,起始点y,长度，高度），颜色(),厚度)
cv2.rectangle(img, (100, 100, 200, 200), color=(0, 0, 255), thickness=2)

cv2.imshow('img', img)

# 4.等待.毫秒为单位，0代表无限等待，直到按键事件发生
cv2.waitKey(0)

# 5.释放内存,关闭窗口
cv2.destroyAllWindows()
