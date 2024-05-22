from .msg_funcion import (
    media_title_zone,
    now_time,
    get_weather,
    get_msglist,
    psutil_data,
    random_psutil,
    simple_time,
    intact_time,
)

msg_func_dict: dict = {
    "时间": now_time,
    "详细时间": intact_time,
    "简化时间": simple_time,
    "天气": get_weather,
    "媒体标题": media_title_zone.get,
    "固定硬件信息": psutil_data,
    "随机硬件信息": random_psutil,
    "随机消息列表": get_msglist,
}
