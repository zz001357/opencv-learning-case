# -*- coding: utf-8 -*-
# @File:读取图片.py
# @Author: Zhang Ze
# @Date:   2024-07-22
# @Last Modified by:   Zhang Ze


# 1.导入cv模块 【pip install opency-python】 这里安装的是4.10
import cv2

# 2.导入图片
img = cv2.imread('./img/_DSF0488-1.jpg')

# 3.显示图片
# winname为show的框体名，必填
cv2.imshow("GRAY", img)

# 4.等待.毫秒为单位，0代表无限等待，直到按键事件发生
cv2.waitKey(0)

# 5.释放内存,关闭窗口
cv2.destroyAllWindows()
