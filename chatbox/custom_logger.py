# -*- coding: utf-8 -*-


import logging
from logging import handlers
from datetime import datetime

from chatbox import *


class Logger(object):
    level_relations = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "crit": logging.CRITICAL,
    }  # 日志级别关系映射

    def __init__(
        self,
        filename,
        level="info",
        when="D",
        backCount=3,
        out_log=False,
        fmt="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(threadName)s - %(module)s - %(funcName)s: %(message)s",
    ):
        self.logger = logging.getLogger(filename if out_log else __name__)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        sh = logging.StreamHandler()  # 往屏幕上输出
        sh.setFormatter(format_str)  # 设置屏幕上显示的格式
        self.logger.addHandler(sh)  # 把对象加到logger里

        if out_log:  # 当out_log为True时，才添加文件处理器
            th = handlers.TimedRotatingFileHandler(
                filename=filename, when=when, backupCount=backCount, encoding="utf-8"
            )
            th.setFormatter(format_str)  # 设置文件里写入的格式
            self.logger.addHandler(th)

        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别


# Create a global Logger instance
global_logger = Logger(
    f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log',
    level="debug",
    out_log=out_log,
)

log = global_logger.logger
