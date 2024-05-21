# chatbox_project

这是一个为VRChat设计的chatbox工具，它可以在游戏中显示实时信息，增强您的游戏体验。

## 特点

- **实时时间显示**：chatbox会显示当前时间（精确到秒），每3秒刷新一次。您可以在配置文件中修改UTC偏移来调整时间。
- **天气信息**：chatbox会显示您所在地区的天气情况，每30分钟刷新一次。您需要在配置文件中手动设置地区。
- **媒体播放信息**：正在播放的媒体信息会显示在chatbox上。如果标题过长，会使用滚动效果。由于Windows播放器的限制，标题可能会有延迟显示。
- **硬件信息监控**：chatbox可以显示CPU、GPU（目前只支持NVIDIA显卡）、内存、硬盘读写速度及使用率，以及当前网络IO量。
- **网页版聊天栏**：您可以通过程序直接在游戏里的chatbox显示网页输入的内容(单向的，游戏不允许第三方程序读取其他人的chatbox)

## 安装

1. 克隆仓库到本地：
git clone https://github.com/Firework-133/chatbox_project.git
2. 安装所需依赖：
pip install -r requirements.txt
(建议使用虚拟环境)

## 配置
项目的配置文件为 `.json` 格式，您可以通过编辑它来自定义chatbox的行为。

```json
{
    "address": "127.0.0.1", // chatbox服务的IP地址
    "port": 9000, // chatbox服务的端口号
    "path": "/chatbox/input", // chatbox服务的路径
    "type_chatbox": true, // 是否启用打字chatbox功能
    "Web_chatbox": true, // 是否启用网页版chatbox功能
    "webip": "0.0.0.0", // 网页版chatbox服务的IP地址
    "webport": "5001", // 网页版chatbox服务的端口号
    "msglist": [ // 预设的消息列表
        "Hello!",
        "很高兴认识你！"
    ],
    "region": "广州", // 天气信息的地区名称
    "region_id": 101280101, // 天气信息的地区ID
    "weather_url": "http://www.weather.com.cn/weather1d/101280101.shtml", // 天气信息的URL
    "UTC": "+8", // UTC时间偏移量
    "out_log": false, // 是否输出日志到文件
    "random_psutil_list": [ // 随机显示的系统信息列表
        "磁盘 IO 统计信息",
        "磁盘总量",
        "获取内存信息"
    ],
    "psutil_list": [ // 固定显示的系统信息列表
        "获取CPU和GPU使用情况",
        "网络 IO 统计信息"
    ]
}

```
## 使用
安装完依赖后，激活虚拟环境(如果有选择使用虚拟环境的话)，直接通过main.py启动

## 联系方式
如果您有任何问题或建议，请通过 Issues 联系我。