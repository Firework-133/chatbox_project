# -*- coding: utf-8 -*-

import random

import chatbox
from chatbox import *
from .custom_logger import log
from .psutil_funcion_dict import psutil_func_dict

random_psutil_dict: dict = {}
psutil_dict: dict = {}

# 填充随机psutil字典
for psutil_name in random_psutil_list:
    try:
        random_psutil_dict[psutil_name] = psutil_func_dict[psutil_name]
    except KeyError:
        log.warning("无效功能：%s", psutil_name)

# 填充固定psutil字典
for psutil_name in psutil_list:
    try:
        psutil_dict[psutil_name] = psutil_func_dict[psutil_name]
    except KeyError:
        log.warning("无效功能：%s", psutil_name)


# 随机选择获取信息的函数
def random_get_psutil(random_psutil_dict):
    if not random_psutil_dict:
        return None
    random_psutil_dict_val = list(random_psutil_dict.values())
    random_psutil = random.choice(random_psutil_dict_val)
    if isinstance(random_psutil, dict):
        random_psutil = random.choice(list(random_psutil.values()))
    random_psutil_re = random_psutil()
    return f"-{random_psutil_re}-" if random_psutil_re else None


# 固定获取信息的函数
def get_psutil(psutil_dict: dict):
    if not psutil_dict:
        return None
    psutil_return_list = []
    for psutil_func in psutil_dict.values():
        if isinstance(psutil_func, dict):
            dict_return_list = []
            for sub_psutil_func in psutil_func.values():
                dict_return_list.append(sub_psutil_func())
            psutil_return_list.append(" ".join(filter(None, dict_return_list)))
        else:
            psutil_return_list.append(psutil_func())
    return "\n".join(filter(None, psutil_return_list))
