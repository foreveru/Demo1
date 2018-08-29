# -*- coding: utf-8 -*-
from time import time
from PIL import Image
from io import BytesIO

import os
import cv2
import math
import base64
import logging

def logit(msg):
    print("%s" % msg)

if __name__ == "__main__":
    import shutil
    import argparse
    from datetime import datetime

    import socketio
    import eventlet
    import eventlet.wsgi
    from flask import Flask

    # 创建ArgumentParser()对象
    parser = argparse.ArgumentParser(description='Auto Drive Car Demo')
    # 调用add_argument()方法添加参数
    # 使用parse_args()解析添加的参数
    parser.add_argument('record',type=str, nargs='?', default='', help='Path to image folder to record the images.')
    args = parser.parse_args()
    print(args.record)

    if args.record:
        if not os.path.exists(args.record):
            os.mkdir(args.record)
        logit('Start recording images to %s' % args.record)

    sio = socketio.Server()
    # send control info to auto_car
    def send_control(steering_angle, throttle):
        '''
        :param steering_angle: 方向盘角度
        :param throttle: 油门
        :return: 
        '''




