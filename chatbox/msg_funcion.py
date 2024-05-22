import random

from chatbox import *
from .media_control import get_media_title
from .utc_time_formatter import get_time
from .weather_fetcher import weather_instance
from .hardware_status_tracker import (
    get_psutil,
    psutil_dict,
    random_get_psutil,
    random_psutil_dict,
)


# 消息列表抽签
def get_msglist():
    if msglist:
        return random.choice(msglist)
    return None


def get_weather():
    return weather_instance.get_current_weather()


def now_time():
    return get_time(UTC, "%Y-%m-%d %H:%M:%S %a") + f" UTC{UTC}"


def simple_time():
    return get_time(UTC, simple_time_format) + f" UTC{UTC}"


def intact_time():
    return get_time(UTC, intact_time_format) + f" UTC{UTC}"


def psutil_data():
    return get_psutil(psutil_dict)


def random_psutil():
    return random_get_psutil(random_psutil_dict)


media_title = get_media_title()


class get_media_title_zone:
    def __init__(self, media_title):
        self.media_title = media_title

    def get(self):
        return next(self.media_title)


media_title_zone = get_media_title_zone(media_title)
