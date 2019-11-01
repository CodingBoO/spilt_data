# -*- coding: utf-8 -*-
# @Time    : 2019/11/1 上午9:50
# @Author  : Mat
# @Email   : 735678367@qq.com
# @File    : detect_blur.py.py
# @Software: PyCharm
import argparse
import cv2
from imutils import paths


def variance_of_laplacian(image):
    return cv2.Laplacian(image,cv2.CV_64F).var()

ap=argparse.ArgumentParser()
ap.add_argument("-i","--images",required=True,help="path to input directory of images")
ap.add_argument("-t","--threshold",type=float,default=2000.0,help="focus measure that fall below this value will be considered 'blurry")
args=vars(ap.parse_args())


for imagePath in paths.list_images(args["images"]):
    image=cv2.imread(imagePath)
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    fm=variance_of_laplacian(gray)
    text="Not Blurry"
    if fm<args["threshold"]:
        text="blurry"

    cv2.putText(image,"{}:{:.2f}".format(text,fm),(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255),3)
    cv2.imshow("image",image)
    key=cv2.waitKey(0)