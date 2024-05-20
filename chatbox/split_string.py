# -*- coding: utf-8 -*-


def split_string_by_length(string, min_length, max_length):
    res = []
    temp = ""
    count = 0
    for char in string:
        if (char >= "\u4e00" and char <= "\u9fa5") or char in [
            "；",
            "：",
            "，",
            "（",
            "）",
            "！",
            "？",
            "——",
            "……",
            "、",
            "》",
            "《",
        ]:
            count += 2
        else:
            count += 1
        if count > max_length or (count >= min_length and char == " "):
            res.append(temp)
            temp = "" if char == " " else char
            count = 0 if char == " " else 1 if char < "\u4e00" or char > "\u9fa5" else 2
        else:
            temp += char
    if temp:
        res.append(temp)
    return res
