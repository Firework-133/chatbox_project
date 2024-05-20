# -*- coding: utf-8 -*-


import psutil
import time
import threading

import chatbox
from chatbox import *
from .get_psutil_func_state import get_psutil_state


# 获取网络速度
class NetSpeedMonitor(threading.Thread):
    def __init__(self, name=None):
        super().__init__(name=name)
        self.download_speed = 0
        self.upload_speed = 0
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            # 获取网络接口信息
            net1 = psutil.net_io_counters()

            # 等待一秒
            time.sleep(1)

            # 再次获取网络接口信息
            net2 = psutil.net_io_counters()

            # 计算下载和上传速度
            self.download_speed = (net2.bytes_recv - net1.bytes_recv) / 1024 / 1024
            self.upload_speed = (net2.bytes_sent - net1.bytes_sent) / 1024 / 1024

    def get_speeds(self):
        return self.download_speed, self.upload_speed

    def stop(self):
        self.running = False


# 创建一个NetSpeedMonitor对象
monitor = NetSpeedMonitor(name="网络速度监控线程")


# 这里可以执行其他任务，而get_net_speed函数会在后台运行
# 当需要获取网速时，调用get_speeds函数
@get_psutil_state
def net_io_counters() -> str:
    download, upload = monitor.get_speeds()
    return f"下载/上传:{download:.2f}/{upload:.2f}Mbps"
