# -*- coding: utf-8 -*-


import gpustat
import psutil
import pynvml

import chatbox
from chatbox import *

from .custom_logger import log
from .get_psutil_func_state import get_psutil_state


@get_psutil_state
def get_cpu_usage() -> str:
    # 获取CPU使用情况
    cpu_usage = psutil.cpu_percent()
    return f"CPU:{cpu_usage}%"


# 使用gpustart
# 默认显示第一个显卡的参数(你不会真的买得起显卡交火吧.....)
def gpustat_new_query():
    try:
        gpu_stats = gpustat.GPUStatCollection.new_query()
    except pynvml.NVMLError_LibraryNotFound as e:
        gpu_stats = None
        log.warning("GPU信息获取失败：未安装英伟达驱动,暂时只支持英伟达显卡(AMD悲)")
    except pynvml.NVMLError_NoPermission as e:
        gpu_stats = None
        log.error("GPU信息获取发生错误,硬件错误: %s", e, exc_info=True)
    except Exception as e:
        gpu_stats = None
        log.error("GPU信息获取发生错误,未知错误: %s", e, exc_info=True)
    return gpu_stats


# 获取GPU检测实例
gpu_stats = gpustat_new_query()


@get_psutil_state
def get_gpu_usage() -> str:
    if gpu_stats:  # 检测当前GPU数据是否可以被读取
        # 在函数内部调用gpustat_new_query来刷新GPU状态
        gpus = gpu_stats.gpus
        gpu_usage = gpus[0].utilization
        # 只读取第一个GPU(不支持显卡交火)
    else:
        gpu_usage = "-"
    return f"GPU:{gpu_usage}%"


@get_psutil_state
def get_memory_usage() -> str:
    # 获取内存总量，并转换为GB
    memory_usage = psutil.virtual_memory()
    memory_total_gb = memory_usage.total / (2**30)
    memory_used_gb = memory_usage.used / (2**30)
    return f"内存:{memory_total_gb:.2f}/{memory_used_gb:.2f}GB,{memory_usage.percent}%"


# 随机获取硬件状态
@get_psutil_state
def disk_io_counters() -> str:
    # 查看磁盘 IO 统计信息，并转换为GB
    disk_io_counters = psutil.disk_io_counters()
    disk_read_gb = disk_io_counters.read_bytes / (2**30)
    disk_write_gb = disk_io_counters.write_bytes / (2**30)
    return f"磁盘读/写:{disk_read_gb:.2f}/{disk_write_gb:.2f}GB"


@get_psutil_state
def disk_usage() -> str:
    # 获取磁盘总量，并转换为GB
    disk_usage = psutil.disk_usage("/")
    disk_total_gb = disk_usage.total / (2**30)
    disk_used_gb = disk_usage.used / (2**30)
    return f"磁盘:{disk_total_gb:.2f}/{disk_used_gb:.2f}GB,{disk_usage.percent}%"
