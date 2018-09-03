# -*- coding:utf-8 -*-
import cv2, os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def rad2deg(radian):
    '''
    :param radian: 弧度
    :return: 角度
    '''
    return radian / np.pi * 180.0

def deg2rad(degree):
    '''
    :param degree: 角度
    :return: 弧度
    '''
    return degree/180.0 * np.pi

def crop_image(img):
    bottom_half_ratios = (0.55, 1.0)

    bottom_half_slice = slice(*(int(x * img.shape[0]) for x in bottom_half_ratios)) #slice(132,240,None)
    print(bottom_half_slice)
    bottom_half = img[bottom_half_slice, :, :]


def bgr2rgb(img):
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return rgb_img

def preprocess(image):
    '''
    Combine all preprocess functions into one
    :param img: current processed image
    :return: image that processed
    '''
    image = crop_image(image)
    # image = resize(image)
    # image = rgb2yuv(image)
    return image

if __name__ == '__main__':
    imgpath='D:\F_Section\My Project\IntelligentCar\TrendFormula\Demo1\img\eagle_2018_09_02_18_02_37_526.jpg'
    img = Image.open(imgpath)  # 打开图片
    #img.show()
    img = np.asarray(img) #一个矩阵 img.shape=(240,320,3) RGB


    img2 = img[slice(132,240,None),:,:]
    print(img2.shape)
    #preprocess(img)



    # im = cv2.imread(imgpath) #BGR
    # im2 = bgr2rgb(im) #RGB
    # cv2.imshow("original pic", im)
    # cv2.waitKey()
    #
    fig = plt.figure()
    plt.subplot(121)
    plt.imshow(img)
    plt.subplot(122)
    plt.imshow(img2)
    plt.show()



