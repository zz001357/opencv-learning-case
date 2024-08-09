# -*- coding: utf-8 -*-
# @File:视频检测.py
# @Author: Zhang Ze
# @Date:   2024-07-24
# @Last Modified by:   Zhang Ze

import cv2


def face_detect_def(frame):
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 1.转成灰度图
    '''
        调用opencv级联分类器分类，detectMultiScale()出人脸对应位置。输出的人脸外接矩形坐标
        调整detectMultiScale()的参数可以使检测结果更加精确
        1.image表示的是要检测的输入图像
        2.scaleFactor表示在前后两次相继的扫描中，搜索窗口的缩放比例。搜索窗口大小会影响搜索效果
        3.minNeighbors表示构成检测目标的相邻矩形的最小个数。默认情况下，该值为 3，
                      意味着有 3 个以上的检测标记存在时，才认为人脸存在。如果希望提高检测的准确率，
                      可以将该值设置得更大，但同时可能会让一些人脸无法被检测到。
        4.flags该参数通常被省略。在使用低版本 OpenCV（OpenCV 1.X 版本）时，
               它可能会被设置为 CV_HAAR_DO_CANNY_PRUNING，
               表示使用 Canny 边缘检测器来拒绝一些区域。
        5.minSize目标的最小尺寸，小于这个尺寸的目标将被忽略。
        6.maxSize目标的最大尺寸，大于这个尺寸的目标将被忽略。
    '''
    haarcascades = 'D:/PyProjects/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml'
    faces = cv2.CascadeClassifier(haarcascades).detectMultiScale(gray_img)
    print("faces-----", faces)
    if len(faces) != 0:
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)


'''
# 1.导入摄像头数据
VideoCapture()既支持从视频文件(.avi ， .mpg格式)读取，也支持直接从摄像机(比如电脑自带摄像头)中读取
read()读取视频流数据中的一帧
isOpened()检查当前的cv2.VideoCapture是否已经打开。
release()：释放cv2.VideoCapture对象占用的资源。


VideoCapture(0)中参数是0，表示打开笔记本的内置摄像头，如果有多个摄像头，往上加就可。

'''
cap = cv2.VideoCapture('./video/v2.mp4')
while True:
    flag, frame = cap.read()
    if not flag:
        break
    face_detect_def(frame)
    cv2.imshow("video", frame)
    '''
    等待键盘响应，该函数中可以传入具体的毫秒数，表示程序等待键盘输入的时间，
    如果传入特定的毫秒数，则特定毫秒数内按下任意键会返回该键的ASCII码值，程序将会继续运行；
    如果没有键盘输入则返回-1；如果传入参数为0，则表示持续等待键盘输入，该函数常用于检测是否有特定的键被按下。
    '''
    keyNum = cv2.waitKey(1)
    # 按钮关闭
    if cv2.getWindowProperty('video', cv2.WND_PROP_VISIBLE) < 1:
        break
    # 按ESC关闭
    if keyNum == 27:
        break

# 5.释放内存,关闭窗口
cv2.destroyAllWindows()
# 6.释放摄像头,关闭窗口
cap.release()
