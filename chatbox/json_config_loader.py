# -*- coding: utf-8 -*-
import json


class Config:
    def __init__(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            self.data = json.load(file)

    def __getattr__(self, item):
        # return self.data.get(item)
        if item not in self.data:
            raise AttributeError(f"配置参数 '{item}' 不存在。")
        return self.data.get(item)
