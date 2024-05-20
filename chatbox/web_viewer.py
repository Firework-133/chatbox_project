# -*- coding: utf-8 -*-


from flask import Flask, render_template, request
import logging
import threading


from chatbox import *
from .chatbox import osc_message
from .custom_logger import log


# 感谢neko_a2942
# https://a2942.top:5904/a2942/OSC/
# 提供的Flask页面及后台

# 替换日志记录器
werkzeug_logger = logging.getLogger("werkzeug")
for handler in werkzeug_logger.handlers[:]:
    werkzeug_logger.removeHandler(handler)
werkzeug_logger.addHandler(log)

# 调用库flask
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])  # 接收来自GET和POST的表单数据
def home():
    if request.method == "POST":  # 如果接收到POST消息
        if "message" in request.form:  # 如果收到message的数据
            message = request.form["message"]
            osc_message.set_message(message)
            # 为message赋值获取的表单信息的message的数据
            # 消息格式可参考"https://docs.vrchat.com/docs/osc-as-input-controller"(官方帮助文档，推荐)
            # 或"https://a2942.top:5904/a2942/OSC/"(自己根据上面的内容写的，可能有翻译错误的位置)

    return render_template("index.html")


def run_app():
    app.run(
        debug=True, host=webip, port=webport, use_reloader=False
    )  # 运行在本地的网页服务器


# 创建一个线程来运行Flask应用
flask_thread = threading.Thread(target=run_app, name="网页聊天栏")
# 设置为守护线程，确保主程序退出时线程也会退出
flask_thread.daemon = True
# 这里可以继续执行其他主程序的代码
