# -*- coding: utf-8 -*-


import sys,os
import atexit
import schedule
import time

import chatbox
from chatbox import *
from .chatbox import sender, chatbox_main
from .custom_logger import log
from .net_io_speed import monitor
from .web_viewer import flask_thread
from .media_control import fetcher


# 载入线程
def init():
    log.info("准备中")
    if Web_chatbox is True:
        flask_thread.start()
        os.system(f"start http://{"localhost" if webip == "0.0.0.0" else webip}:{webport}")
    monitor.start()
    fetcher.start()
    log.info("线程启动完成")


# 退出线程
def shutdown():
    try:
        monitor.stop()
        fetcher.stop()
        sender.send_message(path, ("", type_chatbox))
    finally:
        pass


# 退出时执行
@atexit.register
def when_exit():
    # 防止意外退出
    shutdown()
    log.info("程序已退出")


# 主函数
def main() -> None:
    try:
        # 启动线程
        init()
        log.info("开始运行，按Ctrl+C退出")
        schedule.every(3).seconds.do(chatbox_main).tag("chatbox_main")
        chatbox_main()
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        log.info("退出中.....")
    except Exception as e:
        log.error("程序出现错误：%s", e, exc_info=True)
        log.info("退出中.....")
    finally:
        log.info("退出线程中")
        shutdown()
        log.info("线程退出完成")
        sys.exit() #现在不是唯一的退出点
