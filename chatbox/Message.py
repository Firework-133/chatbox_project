import schedule


class OscMessage:
    def __init__(self):
        self.message: str = ""
        self.msg_trake: bool = False
        # 安排定时重置消息
        schedule.every(30).seconds.do(self.reset_message).tag("reset_message")

    def set_message(self, message: str) -> None:
        self.message = message
        self.msg_trake: bool = True
        # 重置定时任务
        schedule.clear("reset_message")
        schedule.every(30).seconds.do(self.reset_message).tag("reset_message")

    def reset_message(self) -> None:
        """重置消息内容"""
        self.message = ""
