# -*- coding: utf-8 -*-


import urllib.request
import re
import schedule

import chatbox
from chatbox import *
from .custom_logger import log


def get_weather(place: str, url: str) -> str:
    try:
        res1 = urllib.request.urlopen(url, timeout=5)
        date = res1.read().decode("utf8")
        pattern = re.compile(r'value="(.*?)" /')
        res2 = re.findall(pattern, date)
        str_weather = place + ":" + res2[1]
        weather = str_weather[0:3] + str_weather[17:32]
    except urllib.error.URLError as e:
        log.error("无法获取天气,网络错误：%s", e, exc_info=True)
        return None
    except ConnectionRefusedError as e:
        log.error("无法获取天气,服务器错误：%s", e, exc_info=True)
        return None
    return weather


class Weather:
    def __init__(self, region, weather_url):
        self.region = region
        self.weather_url = weather_url
        self.now_weather = get_weather(region, weather_url)

    def update_weather(self):
        self.now_weather = get_weather(self.region, self.weather_url)

    def get_current_weather(self):
        return self.now_weather


# 创建Weather类的实例
weather_instance = Weather(region, weather_url)


# 定时任务，用于更新天气
def scheduled_task():
    weather_instance.update_weather()


schedule.every(30).minutes.do(scheduled_task)
