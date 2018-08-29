# -*- coding: utf-8 -*-
from time import time
from PIL import Image
from io import BytesIO

import os
import cv2
import math
import base64
import logging

import shutil
import argparse
from datetime import datetime

import socketio
import eventlet
import eventlet.wsgi
from flask import Flask

def logit(msg):
    print("%s" % msg)


# send control info to auto_car
def send_control(steering_angle, throttle):
    '''
    :param steering_angle: 方向盘角度
    :param throttle: 油门
    :return: 
    '''


if __name__ == "__main__":
    # 创建ArgumentParser()对象
    parser = argparse.ArgumentParser(description='Auto Drive Car Demo')
    # 调用add_argument()方法添加参数
    # 使用parse_args()解析添加的参数
    parser.add_argument('record',type=str, nargs='?', default='', help='Path to image folder to record the images from the run.')
    args = parser.parse_args()
    print(args.record)

    if args.record:
        if not os.path.exists(args.record):
            os.mkdir(args.record)
        logit('Path to image folder: %s' % args.record)

    # initialize socketio server
    sio = socketio.Server()
    # our flask(web) app
    app = Flask(__name__)
    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sio, app)
    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('',4567)), app)






