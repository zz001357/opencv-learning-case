# -*- coding: utf-8 -*-
# @File:数据训练.py
# @Author: Zhang Ze
# @Date:   2024-07-24
# @Last Modified by:   Zhang Ze
import datetime
import os
import time

import cv2
import numpy as np

'''
流程
    训练数据
        读取全部数据
        训练数据
        保存数据
'''


def get_image_label(path):
    image_paths = []  # 所有图片路径
    face_samples = []  # 人脸数据
    ids = []  # 身份编号
    labels_list = []  # 模型标签编号
    # 加载分类器
    haarcascades = 'D:/PyProjects/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml'
    face_cascade = cv2.CascadeClassifier(haarcascades)
    # 获取faces路径下的所有文件夹
    dirs = os.listdir(path)
    # os.listdir()返回指定路径下的文件和文件夹列表
    # 获取每一个文件夹下的图片路径
    for f in dirs:
        f_path = os.path.join(path, f)
        for i in os.listdir(f_path):
            id = int(f.split('_')[0])
            ids.append(id)
            image_paths.append(os.path.join(f_path, i))
    # 遍历图片，获取 对应标签和图片，这里以图片顺序为标签
    for n, imagePath in enumerate(image_paths):
        index = ids[n]
        img = cv2.imread(imagePath)
        # 统一尺寸
        resize_img = cv2.resize(src=img, dsize=(295, 413))
        gray_img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)
        # 人脸检测
        face = face_cascade.detectMultiScale(gray_img, 1.3, 5,0)
        print("发现{0}个人脸!".format(len(face)))

        # 遍历人脸
        for (x, y, w, h) in face:
            cv2.rectangle(resize_img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
            # 添加人脸数据
            face_samples.append(gray_img[y:y + h, x:x + w])
            labels_list.append(index)

    # 返回人脸数据和模型标签编号
    return face_samples, labels_list


if __name__ == '__main__':

    # 模型路径
    path = './faces/'
    # 获取人脸数据和身份信息
    face_samples_list, labels_list = get_image_label(path)
    print(labels_list)
    print(face_samples_list)

    # 导入人脸识别模型
    # 使用LBPHFaceRecognizer_create()函数创建的人脸识别模型可以用于 训练 和 识别
    # 训练过程中，‌需要提供一组人脸图像及其对应的标签（‌通常是人的身份信息）‌。
    # ‌训练完成后，‌模型可以用于实时的人脸识别，‌即通过输入一张人脸图像，
    # ‌模型可以识别出图像中的人脸是否在训练集中出现过，‌如果出现过，‌还可以给出具体的身份信息。‌
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # # 训练模型
    recognizer.train(face_samples_list, np.array(labels_list))

    # 保存模型
    recognizer.save('./face_yml/face_data.yml')
