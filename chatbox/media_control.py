# -*- coding: utf-8 -*-


import platform

from .custom_logger import log

if platform.system() == "Windows":
    from .winsdk_media_control import fetcher, get_media_title
else:
    from .unknown_media_control import fetcher, get_media_title
