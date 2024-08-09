# -*- coding: utf-8 -*-
# @File:人脸识别.py
# @Author: Zhang Ze
# @Date:   2024-07-27
# @Last Modified by:   Zhang Ze

import cv2

'''
流程
    人脸识别
        打开摄像头
        检测人脸
        识别人脸
'''
win_name = '人脸识别'  # 识别框名字
haarcascades = 'D:/PyProjects/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml'
# 导入人脸识别模型
# 使用LBPHFaceRecognizer_create()函数创建的人脸识别模型可以用于 训练 和 识别
# 训练过程中，‌需要提供一组人脸图像及其对应的标签（‌通常是人的身份信息）‌。
# ‌训练完成后，‌模型可以用于实时的人脸识别，‌即通过输入一张人脸图像，
# ‌模型可以识别出图像中的人脸是否在训练集中出现过，‌如果出现过，‌还可以给出具体的身份信息。‌
recognizer = cv2.face.LBPHFaceRecognizer_create()
# 读取训练集
recognizer.read('./face_yml/face_data.yml')
# 调用摄像头获取人脸数据
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
if cap.isOpened():
    while True:
        ret, frame = cap.read()
        if ret is True:
            # 灰度转换
            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face = cv2.CascadeClassifier(haarcascades).detectMultiScale(gray_img, 1.5, 5, minSize=(285, 285),
                                                                        maxSize=(286, 286))
            # 判断是否检测到人脸
            if len(face) != 0:
                for x, y, w, h in face:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
                    # 人脸识别
                    id, confidence = recognizer.predict(gray_img[y:y + h, x:x + w])

                    # 创建摄像头前置的文字框,使用中文会乱码，需要加载工具
                    cv2.putText(frame, 'face', (x + 8, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 3)
                    print(id)
                    print(confidence)
            else:
                print("没有检测到人脸")
            cv2.imshow(win_name, frame)
            keyNum = cv2.waitKey(1)
            # 按钮关闭
            if cv2.getWindowProperty(win_name, cv2.WND_PROP_VISIBLE) < 1:
                break
            # 按ESC关闭
            if keyNum == 27:
                break
    # 5.释放内存,关闭窗口
    cv2.destroyAllWindows()
    # 6.释放摄像头,关闭窗口
    cap.release()
else:
    print("镜头没打开")
