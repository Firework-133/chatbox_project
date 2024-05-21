# -*- coding: utf-8 -*-
import json
import traceback

from .json_config_loader import Config

try:
    # 创建Config对象时自动加载配置
    config = Config("config.json")

    address: str = config.address
    port: int = config.port
    path: str = config.path
    type_chatbox: bool = config.type_chatbox
    Web_chatbox: bool = config.Web_chatbox
    webip: str = config.webip
    webport: str = config.webport
    msglist: list[str] = config.msglist
    region: str = config.region
    region_id: int = config.region_id
    weather_url: str = config.weather_url
    UTC: str = config.UTC
    out_log: bool = config.out_log

    random_psutil_list: list = config.random_psutil_list
    psutil_list: list = config.psutil_list

except FileNotFoundError as e:
    print("===未找到config.json文件，使用默认配置===")
    from .default_config import *

except json.decoder.JSONDecodeError as e:
    print("======json格式错误======")
    traceback.print_exc()
    print("======使用默认配置======")
    from .default_config import *

except Exception as e:
    print("===解析json文件时发生未知错误===")
    traceback.print_exc()
    print("======使用默认配置======")
    from .default_config import *
