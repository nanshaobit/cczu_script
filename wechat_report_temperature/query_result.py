# @DateTime     : 2021-10-20 11:46
# @Author       : Nanshao
# @Mail         : Nanshao@n-s.fun
# @Description  :

# 修改为你的UID / 抓包可得
import requests

uid = ""
with requests.get("http://yuyue.cczu.edu.cn:8081/api/healthReporting?userId={}".format(uid), timeout=2) as resp:
    print(resp.content.decode())
