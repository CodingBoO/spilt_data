# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 下午2:57
# @Author  : Mat
# @Email   : 735678367@qq.com
# @File    : show_image.py
# @Software: PyCharm
import cv2 as cv
import os
import shutil
images_path='/apps/LIUBO/image_retrival/result/feng'
images=sorted(os.listdir(images_path),reverse=True)
#print(os.listdir(images_path)[:10])
num=0
for image in images:
    num+=1
    if num>10000:
        break
    shutil.move(os.path.join(images_path,image),os.path.join('/apps/LIUBO/image_retrival/result/10000',image))
    #img=cv.imread(os.path.join(images_path,image),1)
    #img=cv.resize(img,dsize=None,fx=0.3,fy=0.3)
    #print(os.path.join(images_path,image))
    #cv.imshow('test',img)
    #cv.waitKey()