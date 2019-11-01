# -*- coding: utf-8 -*-
# @Time    : 2019/10/31 上午11:36
# @Author  : Mat
# @Email   : 735678367@qq.com
# @File    : sample.py
# @Software: PyCharm
import os
import shutil
image_dir='/apps/LIUBO/品类/data'
dest_path='/apps/LIUBO/品类/resample'
#os.removedirs(dest_path)
shutil.rmtree(dest_path,True)
if not os.path.exists(dest_path):
    for train_test in ['train','test']:
        for i in range(3,8):
            os.makedirs(os.path.join(dest_path,train_test,str(i)))
dirs=os.listdir(image_dir)
for dir in dirs:
    images_path=os.path.join(image_dir,dir)
    images=os.listdir(images_path)
    num=0
    for image in images:
        num+=1
        if num>5000:
            break
        if num%5==0:
           shutil.copyfile(os.path.join(images_path,image),os.path.join(dest_path,'test',dir,image))
        else:
            shutil.copyfile(os.path.join(images_path, image), os.path.join(dest_path, 'train',dir, image))