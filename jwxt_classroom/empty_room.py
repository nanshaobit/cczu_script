# @DateTime     : 2021-12-25 19:02
# @Author       : Nanshao
# @Mail         : Nanshao@n-s.fun
# @Description  :

import requests
from lxml import etree


def get_empty_rooms(week, day):
    building = "西太湖教学楼"
    url = "http://219.230.159.132/web_jxrw/cx_kb_jseskfb.aspx"

    s = requests.Session()
    data = {
        "__VIEWSTATE": "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",
        "__VIEWSTATEGENERATOR": "44DC6E46", "__VIEWSTATEENCRYPTED": "", "Txtcxxq": "21-22-1", "Btdyjse": "打印",
        "BTretu": "返回", "ScriptManager1": "UpdatePanel1|BTcxjse", "BTcxjse": "查询教室使用"}

    # 教学楼
    data["LBjxl"] = building
    # 星期
    data["LBxq"] = day
    # 周次
    data["LBzc"] = week

    with s.post(url, data=data, timeout=10) as resp:
        html = resp.content.decode()
        dom = etree.HTML(html)
    ls_empty = []
    # 空教室原理： 全天空白
    # 可进一步判断上午、下午的空教室（未实现）
    for tr in dom.xpath("//div[@id='Panel2']//tr")[1:]:
        room = tr.xpath("./th[1]//text()")[0]
        tmp_str = ""
        for td in tr.xpath(".//td")[1:]:
            tmp_str += "".join(td.xpath(".//text()")).replace("\xa0", "")
        if tmp_str == "":
            ls_empty.append(room)
    return ls_empty


if __name__ == '__main__':
    # 空教室（全天）
    # 传入 周次、星期， 返回全天没课的教室列表
    res = get_empty_rooms(7, 5)
    print(res)