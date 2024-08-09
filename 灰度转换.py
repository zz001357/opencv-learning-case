# -*- coding: utf-8 -*-
# @File:灰度转换.py
# @Author: Zhang Ze
# @Date:   2024-07-22
# @Last Modified by:   Zhang Ze

# -*- coding: utf-8 -*-
# @File:img_identify.py
# @Author: Zhang Ze
# @Date:   2024-07-22
# @Last Modified by:   Zhang Ze


# 1.导入cv模块 【pip install opency-python】 这里安装的是4.10
import cv2

# 2.导入图片
img = cv2.imread('./img/_DSF0488-1.jpg')

# 3.将导入的图片转为灰度
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 3.1 将灰度图片显示
cv2.imshow('BGR', gray_img)
# 3.2 写入灰度图片（路径，灰度图）
cv2.imwrite('./img/_DSF1297_gray.jpg', gray_img)

# 4.等待.毫秒为单位，0代表无限等待，直到按键事件发生
cv2.waitKey(0)

# 5.释放内存,关闭窗口
cv2.destroyAllWindows()
