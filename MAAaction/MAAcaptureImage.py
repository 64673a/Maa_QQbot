from flask import *
import base64
from io import BytesIO
from PIL import Image
import json
import time

import pyautogui

import MAAaction.createTaskId

app = Flask(__name__)


def base64ToImage(base64Str,filePath):#将base64字符串转图片
    imageData = base64.b64decode(base64Str)
    image = Image.open(BytesIO(imageData))
    image.save(filePath) 


@app.route("/reportStatus",methods=['GET','POST'])#MAA汇报任务端口
def reportStatus():
    global tasks
    report = request.get_json()
    print(report['task'])
    if "HeartBeat" in report['task']:
        time.sleep(3)
        tasks={
            'tasks':
            [
                {
                    "id": MAAaction.createTaskId.createTaskId("CaptureImageNow"),
                    "type": "CaptureImageNow",
                },
            ],
        }

    if "CaptureImage" in report['task']:
        #imgBase64=report['payload']
        base64ToImage(report['payload'],"./image/image1.png")#存储图片
        pyautogui.hotkey('ctrl', 'c')
    return "200"

@app.route("/getTask",methods=['GET','POST'])#发送任务端口
def getTask():
    return json.dumps(tasks)
def MAAcaptureImage():
    global tasks
    tasks={
    'tasks':
    [
        {
            "id": MAAaction.createTaskId.createTaskId("LinkStart-WakeUp"),
            "type": "LinkStart-WakeUp",
        },
        {
            "id":  MAAaction.createTaskId.createTaskId("HeartBeat"),
            "type": "HeartBeat",
        },
    ],
    }
    app.run()