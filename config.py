# -*- coding: utf-8 -*-


address: str = "127.0.0.1"
port: int = 9000
path: str = "/chatbox/input"
type_chatbox: bool = True
Web_chatbox: bool = True
webip: str = "0.0.0.0"  # WEB服务器的IP地址,"0.0.0.0"代表计算机的任何ip都可连接
webport: str = "5001"  # WEB服务器的端口
msglist: list[str] = [
    "Nya~~~",
    "Hello!",
    "我很可爱，请给我钱~~~",
    "OvO*id",
    "QAQ",
    "喵~~~",
    "求贴贴~~~",
    "rua~",
    "OvO",
    "嘿嘿~~~",
    "呵呵~~~",
    "ZZZ~~~",
    "呼噜呼噜",
    "嚯嚯！",
    "咕~~~~",
]
region: str = "广州"
region_id: int = 101280101
weather_url: str = f"http://www.weather.com.cn/weather1d/{region_id}.shtml"
UTC: str = "+8"
out_log: bool = False

random_psutil_list: list = ["磁盘 IO 统计信息", "磁盘总量", "获取内存信息"]
psutil_list: list = ["获取CPU和GPU使用情况", "网络 IO 统计信息"]

Wrap: str = " " * 35
