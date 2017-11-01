import os
import numpy as np
import cv2 as cv
from PIL import Image

data_dir_paths = './dataset/'
folder_lists = os.listdir(data_dir_paths)
print(folder_lists)

# データ整形
data = []
for folder in folder_lists:
    data_dir_path = data_dir_paths + str(folder)
    file_lists = os.listdir(data_dir_path)
    for file_name in file_lists:
        if file_name.endswith('.png'):
            image_path = str(data_dir_path) + '/' + str(file_name)
            image = cv.imread(image_path)
            image = cv.resize(image,(32,32))
            image = image[:,:,::-1]
            image = image.transpose(2,0,1)
            image = (image-127.5)/127.5
            data.append(image)

#ラベリング
cluster = []
count = 0
for folder in folder_lists:
    data_dir_path = data_dir_paths + '/' + str(folder)
    file_lists = os.listdir(data_dir_path)
    for file_name in file_lists:
        if file_name.endswith('.png'):
            cluster.append(count)
    count += 1

#npyファイルへ
label_array = np.array(cluster)
print(label_array.shape)
np.save('face_label.npy',label_array)

data_array = np.array(data)
print(data_array.shape)
np.save('face_data.npy',data_array)
