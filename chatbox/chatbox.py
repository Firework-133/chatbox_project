# -*- coding: utf-8 -*-

from pythonosc import udp_client
import time
import random

import chatbox
from chatbox import *
from .custom_logger import log
from .media_control import get_media_title
from .hardware_status_tracker import (
    get_psutil,
    psutil_dict,
    random_get_psutil,
    random_psutil_dict,
)
from .utc_time_formatter import get_time
from .weather_fetcher import weather_instance
from .Message import OscMessage


media_title = get_media_title()


def send_chatbox_now(func):
    def send_chatbox(*args):
        return_args = func(*args)
        chatbox_main()
        return return_args

    return send_chatbox


class chatbox_OscMessage(OscMessage):
    def __init__(self):
        super().__init__()

    @send_chatbox_now
    def set_message(self, message: str) -> None:
        return super().set_message(message)


# 创建OscMessage实例
osc_message = chatbox_OscMessage()


# 消息列表抽签
def get_msglist():
    if msglist:
        return random.choice(msglist)
    return None


def Simple_msg_list():
    msg_list: list = [
        get_time(UTC, "%H:%M:%S %a") + f" UTC{UTC}",
        next(media_title),
    ]
    return msg_list


def intact_msg_list():
    msg_list: list = [
        get_time(UTC, "%Y-%m-%d %H:%M:%S %a") + f" UTC{UTC}",
        weather_instance.get_current_weather(),
        next(media_title),
        get_psutil(psutil_dict),
        random_get_psutil(random_psutil_dict),
        get_msglist(),
    ]
    return msg_list


# OSC
sender = udp_client.SimpleUDPClient(address, port)


def chatbox_main():
    if osc_message.message:
        msg_list = Simple_msg_list()
        msg_list.append(f"===聊天框===\n \n{osc_message.message}\n ")
    else:
        msg_list = intact_msg_list()
        sender.send_message(path, ("", type_chatbox))
        time.sleep(0.1)
    while None in msg_list:
        msg_list.remove(None)
    str_chatbox: str = "\n".join(msg_list)
    sender.send_message(path, (str_chatbox, type_chatbox))
    log.info("\n%s", str_chatbox)
