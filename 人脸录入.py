# -*- coding: utf-8 -*-
# @File:人脸录入.py
# @Author: Zhang Ze
# @Date:   2024-07-25
# @Last Modified by:   Zhang Ze
import time

import cv2

'''
流程
    人脸录入
        打开摄像头
        输入名字
        检测人脸
        保存图片
'''


# 1.调用摄像头
# CAP_DSHOW,opencv提供捕获摄像头api，用于初始化摄像头参数信息
cap = cv2.VideoCapture(0)

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# # 设置摄像头设备分辨率
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# # 设置摄像头设备帧率,如不指定,默认600
# cap.set(cv2.CAP_PROP_FPS, 24)
if cap.isOpened():
    while True:
        # 3.得到帧图像
        ret, V_show = cap.read()
        if ret is True:
            # 4.显示图像
            cv2.imshow('video', V_show)
            # 5.等5毫秒检测键盘输入
            k = cv2.waitKey(5)
            # 按钮关闭
            if cv2.getWindowProperty('video', cv2.WND_PROP_VISIBLE) < 1:
                break
            # 按s保存，使用ord转换Unicode码点
            if k == ord('s'):
                print("保存")
                save_time = time.time()
                cv2.imwrite("./save_data/" + str(save_time) + ".jpg", V_show)
        else:
            print("没有取到画面")
            break
else:
    print("没打开")
cap.release()
cv2.destroyAllWindows()
