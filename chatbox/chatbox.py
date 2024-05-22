# -*- coding: utf-8 -*-

from pythonosc import udp_client
import time


import chatbox
from chatbox import *
from .custom_logger import log
from .msg_funcion_dict import msg_func_dict
from .Message import OscMessage


Simple_msg_func_list = []
intact_msg_func_list = []


# 填充Simple_msg
for func_name in Simple_msg_list:
    try:
        Simple_msg_func_list.append(msg_func_dict[func_name])
    except KeyError:
        log.warning("无效功能：%s", func_name)

# 填充固定intact_msg
for func_name in intact_msg_list:
    try:
        intact_msg_func_list.append(msg_func_dict[func_name])
    except KeyError:
        log.warning("无效功能：%s", func_name)


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


def Simple_msg_re_list():
    msg_list: list = []
    for func in Simple_msg_func_list:
        msg_list.append(func())
    return msg_list


def intact_msg_re_list():
    msg_list: list = []
    for func in intact_msg_func_list:
        msg_list.append(func())
    return msg_list


# OSC
sender = udp_client.SimpleUDPClient(address, port)


def chatbox_main():
    if osc_message.message:
        msg_list = Simple_msg_re_list()
        msg_list.append(f"===聊天框===\n \n{osc_message.message}\n ")
    else:
        msg_list = intact_msg_re_list()
        sender.send_message(path, ("", type_chatbox))
        time.sleep(0.1)
    while None in msg_list:
        msg_list.remove(None)
    str_chatbox: str = "\n".join(msg_list)
    sender.send_message(path, (str_chatbox, type_chatbox))
    log.info("\n%s", str_chatbox)
