# WS client example

#-----------------------------------------------------------------------#
#   predict.py将单张图片预测、摄像头检测、FPS测试和目录遍历检测等功能
#   整合到了一个py文件中，通过指定mode进行模式的修改。
#-----------------------------------------------------------------------#
import time

import cv2
import numpy as np
from numpy import mean
from PIL import Image
from utils_node import *
from yolo import YOLO
import asyncio
import websockets

async def node_detect():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        count = 0
        while True:
            count += 1
            # name = input("What's your name? ")
            name = str(count)
            await websocket.send(name)
            print(f"> {name}")

            greeting = await websocket.recv()
            print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(node_detect())
