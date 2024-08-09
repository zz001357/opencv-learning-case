# -*- coding: utf-8 -*-
# @File:绘制图形.py
# @Author: Zhang Ze
# @Date:   2024-07-22
# @Last Modified by:   Zhang Ze


# 1.导入cv模块 【pip install opency-python】 这里安装的是4.10
import cv2

# 2.导入图片
img = cv2.imread('./img/_DSF0488-1.jpg')

# 3.绘制图像

# 3.1.绘制矩形(图像，（起始点,起始点,长度，高度），颜色(RGB值),厚度)
cv2.rectangle(img, (100, 100, 200, 200), color=(0, 0, 255), thickness=2)
# 3.2.绘制直线(图像，（起始点坐标）,（终点坐标）,颜色(RGB值),厚度)
cv2.line(img, (100, 100), (300, 300), color=(0, 0, 255), thickness=2)
# 3.3 绘制圆形(图像，（圆心坐标）,半径,颜色(RGB值),厚度)
cv2.circle(img, (500, 500), 100, color=(0, 0, 255), thickness=2)
# 3.4 绘制椭圆(图像，（圆心坐标）,椭圆的半长轴和半短轴长度，椭圆的旋转角度，椭圆弧的起始角度，椭圆弧的结束角度，颜色(RGB值),厚度)
cv2.ellipse(img, (500, 500), (100, 200), 0, 0, 360, color=(0, 0, 255), thickness=2)
cv2.imshow('img', img)

# 4.等待.毫秒为单位，0代表无限等待，直到按键事件发生
cv2.waitKey(0)

# 5.释放内存,关闭窗口
cv2.destroyAllWindows()
