# -*- coding: utf-8 -*-
# @Time    : 2019/10/26 上午11:45
# @Author  : Mat
# @Email   : 735678367@qq.com
# @File    : str.py
# @Software: PyCharm
import os
str_a='/mydata/scene_data/val/1/2036_2015457_11784415.jpg'
print(os.path.splitext(os.path.basename(str_a))[0])
str_a.replace('/','_')
a='_'
print(os.path.splitext(a.join(str_a.split('/')[-3:]))[0])