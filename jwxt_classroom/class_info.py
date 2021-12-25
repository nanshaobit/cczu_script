# @DateTime     : 2021-12-25 18:50
# @Author       : Nanshao
# @Mail         : Nanshao@n-s.fun
# @Description  :


def get_info(cname):
    import requests
    # api地址
    url = "http://jskc.cczu.edu.cn/jwc_req_classinfo.php?classno={}&jxl=教学楼&xq=西太湖校区".format(cname)
    try:
        # 接口太脆弱，人多必崩
        resp = requests.get(url, timeout=15)
    except:
        return False, ""
    import json
    list_r = json.loads(resp.content.decode())
    res = []
    for r in list_r:
        t = {}
        if r["kcm"] == "当前没课":
            t["status"] = False
        else:
            t["status"] = True
            t["name"] = r["kcm"]
            t["teacher"] = r["js"]
            t["jieci"] = r["jc"]
        res.append(t)
    return True, res


def class_room(txt: str):
    err_msg = "请检查输入格式，例：教室 X1阶；教室 X211;注意空格"
    if not txt:
        print(err_msg)
        return
    txt = txt.upper()
    if txt[0] != "X":
        txt = "X" + txt
    if len(txt) == 3 and txt[-1] != "阶":
        print(err_msg)
        return

    import urllib.parse
    # 原始 查询url
    source_url = "http://jskc.cczu.edu.cn/jwc_ewm.php?classno={}&xq=西太湖校区&jxl=教学楼".format(txt)
    print(source_url)
    # 生成二维码 由于接口经常崩， 此二维码生成图片发送到机器人端
    qr_url = "https://nanshaobit.top/qr/?url=" + urllib.parse.quote(source_url)
    # print(url)
    success, res = get_info(txt)

    if success:
        msg = txt + "教室上课信息\n\n节次: 教师 - 课程"
        index = 0
        for i in res:
            index += 1
            msg += "\n{}:".format(index)
            if i["status"]:
                msg += "{}-{}".format(i["teacher"], i["name"])
            else:
                msg += "无人上课"
        print(msg)
        return res
    else:
        print("教室查询服务器异常，请稍后再试")
        return


if __name__ == '__main__':
    # 格式 教室号， X可不写（仅限西太湖校区立德楼）
    # 以下示例均可。
    txt = "211"
    txt = "X211"
    txt = "x211"
    txt = "x8阶"
    txt = "8阶"

    print(class_room(txt))
