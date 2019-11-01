# -*- coding: utf-8 -*-
# @Time    : 2019/10/24 上午9:50
# @Author  : Mat
# @Email   : 735678367@qq.com
# @File    : data.py
# @Software: PyCharm
from PIL import Image
import os
train_image_path='/apps/LIUBO/all_data/train'
imgs=[]
for dir in os.listdir(train_image_path):
    for images in os.listdir(os.path.join(train_image_path,dir)):
        #print("###",images)
        image_path=os.path.join(os.path.join(train_image_path,dir),images)
        label=dir
        print(image_path,label)
        with open(image_path, 'rb') as f:
            img = Image.open(f)
            img=img.convert('RGB')
        imgs.append(img,int(label))
