from flask import *
import base64
from io import BytesIO
from PIL import Image
import json
import time

import pyautogui

import MAAaction.createTaskId

app = Flask(__name__)


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