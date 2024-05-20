# -*- coding: utf-8 -*-


from datetime import datetime, timezone, timedelta

import chatbox
from chatbox import *


# 获取时间
def get_time(utc_offset_str, format_str) -> str:
    # 将偏移量字符串转换为整数
    utc_offset = int(utc_offset_str)

    # 获取当前的UTC时间
    now_utc = datetime.now(timezone.utc)

    # 计算偏移后的当前时间
    now_utc_offset = now_utc + timedelta(hours=utc_offset)

    # 使用指定的格式字符串格式化时间
    return now_utc_offset.strftime(format_str)
