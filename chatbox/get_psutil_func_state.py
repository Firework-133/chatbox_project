# -*- coding: utf-8 -*-


from .custom_logger import log


# 获取硬件状态函数工作状态
def get_psutil_state(func):
    def state():
        try:
            return func()
        except Exception as e:
            psutil_str = None
            log.error("%s 发生错误: %s", func.__name__, e, exc_info=True)
        return psutil_str

    return state
