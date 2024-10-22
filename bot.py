import MAAaction.MAAcaptureImage
import os
import pyautogui

import botpy
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import Message

config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

_log = logging.get_logger()

class MyClient(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")

    async def on_at_message_create(self, message: Message):
        if "/MAA截图" in message.content:
            MAAaction.MAAcaptureImage.MAAcaptureImage()
            await message.reply(file_image="image\\image1.png")
        #if "/Link Start!" in message.content:
            
if __name__ == "__main__":
    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents(public_guild_messages=True)
    client = MyClient(intents=intents)
    client.run(appid=config["appid"], secret=config["secret"])