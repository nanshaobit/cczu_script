# @DateTime     : 2021-10-20 12:57
# @Author       : Nanshao
# @Mail         : Nanshao@n-s.fun
# @Description  :

import requests

"""
所有输入 均未做容错处理。
"""

s = requests.Session()


def get_input_from_ls(ls, k):
    for i, v in enumerate(ls):
        print(f"{i}: -> {v[k]}")

    return ls[int(input("输入序号即可："))]


def get_area():
    ls_area = [{
        "title": "西太湖校区(1-9号楼)",
        "value": '{"area":"西太湖校区","areaname":"西太湖校区"}',
        "aid": "0030000000002501"
    }, {
        "title": "武进校区及西太湖校区(10-11号楼)",
        "value": '{"area":"武进校区","areaname":"武进校区"}',
        "aid": "0030000000002502"
    }]
    return get_input_from_ls(ls_area, "title")


def get_building(area):
    with s.post("http://wxxy.cczu.edu.cn/wechat/callinterface/queryElecBuilding.html", data={
        "aid": area["aid"],
        "account": "100000",
        "area": area["value"],
    }) as resp:
        ls_building = resp.json().get("buildingtab")
        return get_input_from_ls(ls_building, "building")


def get_data(area, building, rid):
    print("query")
    print("*" * 50)
    url = "http://wxxy.cczu.edu.cn/wechat/callinterface/queryElecRoomInfo.html"
    with s.post(url, data={
        "aid": area["aid"],
        "account": "100000",
        "area": area["value"],
        "building": str(building),
        "floor": '{"floorid":"","floor":""}',
        "room": f'{{"room":"","roomid":"{rid}"}}'}) as resp:
        print(resp.json())
        print(resp.json()["errmsg"])


def query():
    area = get_area()
    building = get_building(area)
    rid = input("输入房间号:")
    get_data(area, building, rid)


if __name__ == '__main__':
    query()
