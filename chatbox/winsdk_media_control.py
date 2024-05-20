# -*- coding: utf-8 -*-


import threading
import asyncio
from winsdk.windows.media.control import (
    GlobalSystemMediaTransportControlsSessionManager as MediaManager,
)

# from chatbox import *
from .custom_logger import log
from .split_string import split_string_by_length


# 获取媒体播放内容
class MediaInfoFetcher(threading.Thread):
    def __init__(self, name=None):
        super().__init__(name=name)
        self.media_info = None
        self.loop = asyncio.new_event_loop()
        self.running = False

    def run(self):
        self.running = True
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self.get_media_info_and_position())

    async def get_media_info_and_position(self):
        while self.running:
            sessions = await MediaManager.request_async()
            current_session = sessions.get_current_session()
            if current_session:
                try:
                    info = await current_session.try_get_media_properties_async()
                    self.media_info = {
                        song_attr: getattr(info, song_attr)
                        for song_attr in dir(info)
                        if song_attr[0] != "_"
                    }
                    self.media_info["genres"] = list(self.media_info["genres"])
                except PermissionError as e:
                    log.error("播放器获取错误，重试，详细：%s", e, exc_info=True)
                    self.media_info = None
            else:
                self.media_info = None
            await asyncio.sleep(5)  # 每5秒更新一次

    def get_media_info(self):
        title = self.media_info["title"] if self.media_info else None
        return title

    def stop(self):
        self.running = False


# 使用示例
fetcher = MediaInfoFetcher(name="媒体信息获取线程")


def get_media_title():
    # length = 12
    min_length = 8
    max_length = 14
    while True:
        title = fetcher.get_media_info()
        if title is None:
            yield None
        elif title == "":
            yield "正在播放:[==未知标题==]"
        elif title:
            string = title
            title_list = split_string_by_length(string, min_length, max_length)
            if len(title_list) == 1:
                yield f"正在播放:[{title}]"
            else:
                while (
                    title == fetcher.get_media_info()
                    and title != ""
                    and not title is None
                ):
                    for title_zone in title_list:
                        if title == fetcher.get_media_info() and title:
                            yield f"正在播放:[...{title_zone}...]"
                        else:
                            break
        else:
            yield None
