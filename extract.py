# -*- coding: utf-8 -*-
import cv2
import os
import numpy as np
from PIL import Image

cascade_path = './lbpcascade_animeface.xml'
dir_path_raw = './rawdata/' #元々のデータがあるディレクトリ
dir_path_output = './dataset/' #出力先ディレクトリ

color = (255,255,255)
framenum = 0

file_list = os.listdir(dir_path_raw)
for file_name in file_list:
    image_path = str(dir_path_raw) + str(file_name)
    image = cv2.imread(image_path)
    if not image is None:
        image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        image_gray = cv2.equalizeHist(image_gray)
        cascade = cv2.CascadeClassifier(cascade_path)
        facerect = cascade.detectMultiScale(image_gray,scaleFactor=1.1,minNeighbors=3, minSize=(50, 50))
        if len(facerect) > 0:
            for rect in facerect:
                croped = image[rect[1]:rect[1]+rect[3],rect[0]:rect[0]+rect[2]]
                cv2.imwrite(str(dir_path_output)+'face'+str(framenum)+'.png',croped)
    framenum += 1
