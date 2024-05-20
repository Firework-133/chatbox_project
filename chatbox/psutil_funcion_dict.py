# -*- coding: utf-8 -*-

from .psutil_monitor_func import *
from .net_io_speed import net_io_counters

psutil_func_dict: dict = {
    "磁盘 IO 统计信息": disk_io_counters,
    "磁盘总量": disk_usage,
    "获取内存信息": get_memory_usage,
    "获取CPU和GPU使用情况": {
        "获取CPU使用情况": get_cpu_usage,
        "获取GPU使用情况": get_gpu_usage,
    },
    "获取CPU使用情况": get_cpu_usage,
    "获取GPU使用情况": get_gpu_usage,
    "网络 IO 统计信息": net_io_counters,
}
