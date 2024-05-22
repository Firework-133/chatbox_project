# -*- coding: utf-8 -*-


address: str = "127.0.0.1"
port: int = 9000
path: str = "/chatbox/input"
type_chatbox: bool = True
Web_chatbox: bool = False
webip: str = "0.0.0.0"  # WEB服务器的IP地址,"0.0.0.0"代表计算机的任何ip都可连接
webport: str = "5001"  # WEB服务器的端口
msglist: list[str] = ["Hello!", "很高兴认识你！"]
region: str = "广州"
region_id: int = 101280101
weather_url: str = f"http://www.weather.com.cn/weather1d/{region_id}.shtml"
UTC: str = "+8"
out_log: bool = False

random_psutil_list: list = ["磁盘 IO 统计信息", "磁盘总量", "网络 IO 统计信息"]
psutil_list: list = ["获取CPU和GPU使用情况", "获取内存信息"]
Simple_msg_list: list = ["简化时间", "媒体标题"]
intact_msg_list: list = [
    "详细时间",
    "天气",
    "媒体标题",
    "固定硬件信息",
    "随机硬件信息",
    "随机消息列表",
]
simple_time_format: str = "%Y-%m-%d %H:%M:%S %a"
intact_time_format: str = "%H:%M:%S %a"
