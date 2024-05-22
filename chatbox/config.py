# -*- coding: utf-8 -*-
import json
import os, sys

from .json_config_loader import Config
from . import default_config as defaults

# 配置文件
filename = "config.json"
# 例子
default_config_txt = """

{
    "address": "127.0.0.1",
    "port": 9000,
    "path": "/chatbox/input",
    "type_chatbox": true,
    "Web_chatbox": true,
    "webip": "0.0.0.0",
    "webport": "5001",
    "msglist": [
        "Hello!",
        "很高兴认识你！"
    ],
    "region": "广州",
    "region_id": 101280101,
    "weather_url": "http://www.weather.com.cn/weather1d/101280101.shtml",
    "UTC": "+8",
    "out_log": false,
    "random_psutil_list": [
        "磁盘 IO 统计信息",
        "磁盘总量",
        "获取内存信息"
    ],
    "psutil_list": [
        "获取CPU和GPU使用情况",
        "网络 IO 统计信息"
    ],
    "Simple_msg_list": [
        "简化时间",
        "媒体标题"
    ],
    "intact_msg_list": [
        "详细时间",
        "天气",
        "媒体标题",
        "固定硬件信息",
        "随机硬件信息",
        "随机消息列表"
    ],
    "simple_time_format": "%H:%M:%S %a",
    "intact_time_format": "%Y-%m-%d %H:%M:%S %a"
}

"""

# 尝试加载配置文件
try:
    config = Config(filename)
except FileNotFoundError:
    config = None
    print("未找到config.json文件，尝试生成config.json文件。")
    with open(filename, "w", encoding="utf-8") as file:
        file.write(default_config_txt)
    print("生成成功，请手动配置config.json文件")
    os.system("pause")
    sys.exit()
except json.decoder.JSONDecodeError as e:
    print(f"json格式错误: {e.msg}")
    print("使用默认配置。")
    config = None
except Exception as e:
    print(f"解析json文件时发生未知错误: {e}")
    print("使用默认配置。")
    config = None


# 定义一个辅助函数来获取配置参数
def get_config_param(param_name, default_value):
    if config is not None:
        try:
            value = getattr(config, param_name)
        except AttributeError:
            print(f"缺少参数：{param_name}，使用默认值：{default_value}。")
            return default_value
        else:
            return value
    else:
        print(f"由于配置文件未加载，参数：{param_name} 使用默认值：{default_value}。")
        return default_value


# 单独加载每个参数，如果失败则使用默认值
address = get_config_param("address", defaults.address)
port = get_config_param("port", defaults.port)
path = get_config_param("path", defaults.path)
type_chatbox = get_config_param("type_chatbox", defaults.type_chatbox)
Web_chatbox = get_config_param("Web_chatbox", defaults.Web_chatbox)
webip = get_config_param("webip", defaults.webip)
webport = get_config_param("webport", defaults.webport)
msglist = get_config_param("msglist", defaults.msglist)
region = get_config_param("region", defaults.region)
region_id = get_config_param("region_id", defaults.region_id)
weather_url = get_config_param("weather_url", defaults.weather_url)
UTC = get_config_param("UTC", defaults.UTC)
out_log = get_config_param("out_log", defaults.out_log)
random_psutil_list = get_config_param("random_psutil_list", defaults.random_psutil_list)
psutil_list = get_config_param("psutil_list", defaults.psutil_list)
Simple_msg_list = get_config_param("Simple_msg_list", defaults.Simple_msg_list)
intact_msg_list = get_config_param("intact_msg_list", defaults.intact_msg_list)
simple_time_format = get_config_param("simple_time_format", defaults.simple_time_format)
intact_time_format = get_config_param("intact_time_format", defaults.intact_time_format)
