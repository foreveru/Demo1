# -*- coding: utf-8 -*-
from time import time
from PIL import Image
from io import BytesIO

import os
import cv2
import math
import base64
import logging
import numpy as np

import shutil
import argparse
from datetime import datetime

import socketio
import eventlet
import eventlet.wsgi
from flask import Flask

import utils

def logit(msg):
    print("%s" % msg)

'''
when client sends an event to the server, tha appropriate event handler is invoked with the sid
and the message, which can be a single or multiple arguments.
'''
@sio.on('telemetry')
def telemetry(sid, data):
    if data:
        # get data from client-car
        last_steering_angle = np.pi - float(data['steering_angle'])/180.0 * np.pi
        throttle = float(data['throttle'])
        brake = float(data['brake'])
        speed = float(data['speed'])

        img = Image.open(BytesIO(base64.b64decode(data['image'])))
        img = utils.preprocess(img)
        lap = int(data['lap']) if 'lap' in data else 0
        total_time = data['time']
        status = int(data['status']) if 'status' in data else 0


        # take action
        send_control(0,0)
    else:
        sio.emit('manual',data={}, skip_sid=True
                 )


'''
send control info to auto_car
sio.emit: takes an event name, a message payload of type str, bytes,list,dict,tuple， and the recipient room.
'''
def send_control(steering_angle, throttle):
    '''
    :param steering_angle: 方向盘角度
    :param throttle: 油门
    :return: 
    '''
    sio.emit("steer",
             data={
                 'steering_angle': str(steering_angle),
                 'throttle': str(throttle)
             },
             skip_sid=True)


@sio.on('connect')
def connetc(sid, environ):
    send_control(0, 0)

if __name__ == "__main__":
    # 创建ArgumentParser()对象
    parser = argparse.ArgumentParser(description='Auto Drive Car Demo')
    # 调用add_argument()方法添加参数
    # 使用parse_args()解析添加的参数
    parser.add_argument('record', type=str, nargs='?', default='', help='Path to image folder to record the images from the run.')
    parser.add_argument('model', type=str, help='Path to model h5 file. Model should be on the same path.')
    args = parser.parse_args()

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






