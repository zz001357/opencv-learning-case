# -*- coding: utf-8 -*-
# @File:检测多个.py
# @Author: Zhang Ze
# @Date:   2024-07-24
# @Last Modified by:   Zhang Ze
# -*- coding: utf-8 -*-
# @File:人脸检测.py
# @Author: Zhang Ze
# @Date:   2024-07-22
# @Last Modified by:   Zhang Ze

# 1.导入cv模块 【pip install opency-python】 这里安装的是4.10
import cv2


def face_detect_def(resize_img):
    gray_img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)  # 1.转成灰度图
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
        
        
        haarcascades是opencv模块的联机分类器，训练好的模型作为预识别。
        下载地址 https://opencv.org/releases/
        **Haar特征**、**Haar特征的改进版本（Haar_alt和Haar_alt2）**、**LBP特征**等。
        **Haar_alt2** 在简单背景图像中检测效果较好。   
        **LBP** 在复杂背景图像中的检测效果较好
    '''
    haarcascades = 'D:/PyProjects/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml'
    faces = cv2.CascadeClassifier(haarcascades).detectMultiScale(
        gray_img)
    print("发现{0}个人脸!".format(len(faces)))
    for x, y, w, h in faces:
        cv2.rectangle(resize_img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
    cv2.imshow("face_detect", resize_img)


# 2.导入图片
img = cv2.imread('./img/q.png')

print("修改前", img.shape)
resize_img = cv2.resize(src=img, dsize=(img.shape[1], img.shape[0]))
print("修改后", resize_img.shape)

# 人脸检测
face_detect_def(resize_img)

# 4.等待.毫秒为单位，0代表无限等待，直到按键事件发生
cv2.waitKey(0)

# 5.释放内存,关闭窗口
cv2.destroyAllWindows()
