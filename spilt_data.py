# -*- coding: utf-8 -*-
# @Time    : 2019/10/23 下午2:11
# @Author  : Mat
# @Email   : 735678367@qq.com
# @File    : spilt_data.py
# @Software: PyCharm

import os,shutil
from tqdm import tqdm

image_path='/apps/LIUBO/binggui_xufuji/Xufuji/no_use/JPEGImages'

def spilt_data(image_path,dest_path,class_name):
    images=os.listdir(image_path)
    num=0
    for image in images:
        num+=1
            #print(os.path.join(image_path,image),os.path.join(dest_path,'train',class_name,image))
            #print(os.path.join(image_path, image), os.path.join(dest_path, 'val', class_name))
        if num%5==0 and num%6!=0:
            shutil.copyfile(os.path.join(image_path, image), os.path.join(dest_path, 'val', class_name, image))
        elif num%6==0:
            shutil.copyfile(os.path.join(image_path, image), os.path.join(dest_path, 'test', class_name, image))
        else:
            shutil.copyfile(os.path.join(image_path, image), os.path.join(dest_path, 'train', class_name, image))
        if num==6000:
            break

def resample(image_path,des_path,stride):
    images=os.listdir(image_path)
    num=0
    count=0
    for image in tqdm(images):
        if num%stride==0:
            shutil.copyfile(os.path.join(image_path,image),os.path.join(des_path,image))
            count+=1
            #if(count==3000):
            #    break
        num+=1

if __name__ =="__main__":
    #resample('/apps/LIUBO/binggui/JPEGImages','/apps/LIUBO/binggui_xufuji/冰箱重采样',3)
    spilt_data('/apps/LIUBO/binggui_xufuji/Xufuji/no_use/JPEGImages','/apps/LIUBO/binggui_xufuji/','0')