# @DateTime     : 2021-10-01 11:37
# @Author       : Nanshao
# @Mail         : Nanshao@n-s.fun
# @Description  :
import requests

# 修改为你的UID / 抓包可得
uid = ""

url = "http://yuyue.cczu.edu.cn:8081/api/healthReporting"
"""
Authorization
--
Username: webApp
Password: webApp
"""
headers = {
    "Authorization": "Basic d2ViQXBwOndlYkFwcA==",
    "Referer": "http://yuyue.cczu.edu.cn:8090/"
}

# 数据接口已于(2021-11-06)过时， 请根据readme中的参数填写。
data = {
    "vaccinesState": "2",   # 2021-10-30 新增 疫苗接种情况
    "healthState": "1",
    "healthRemark": "",
    "temperature": "36.4",  # 温度
    "temperatureState": "1",
    "isDangerousArea": "1",
    "dangerousAreaRemark": "",
    "isDangerousPeople": "1",
    "dangerousPeopleRemark": "",
    "isAbroadGat": "1",
    "abroadGatRemark": "",
    "address": "江苏省常州市武进区",  # 地址
    "addressShen": "江苏省",  # 省
    "addressShi": "常州市",  # 市
    "addressXian": "武进区",  # 区/县
    "coordinate": "119.83168806623213,31.71513305947064",  # 经纬度
    "userId": uid,  # 用户ID
    "userJob": "4"
}

with requests.post(url, data=data, headers=headers) as resp:
    # {"data":null,"resp_code":0,"resp_msg":"填报成功！"}
    print(resp.content.decode())
