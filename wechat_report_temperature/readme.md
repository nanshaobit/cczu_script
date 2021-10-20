## 企业微信 每日健康打卡

> UID 需要抓包获得，也可通过查询当日脚本遍历得出(不推荐)。
> 查询当日脚本中， `"deptCode":"X","schoolYear":"X"` 代表 班号、年级 同一个班在一起，按学号升序。

### 上报接口

+ url: `http://yuyue.cczu.edu.cn:8081/api/healthReporting`
+ method: `POST`
+ headers: 
  + `"Authorization": "Basic d2ViQXBwOndlYkFwcA=="` (Username: webApp, Password: webApp)
  + `"Referer": "http://yuyue.cczu.edu.cn:8090/"`  必须
+ data:
``` json
// 除有注释外，其他内容正常情况不需要修改。
{
    "healthState": "1",
    "healthRemark": "",
    "temperature": "36.4", // 体温 建议在区间内随机
    "temperatureState": "1",
    "isDangerousArea": "1",
    "dangerousAreaRemark": "",
    "isDangerousPeople": "1",
    "dangerousPeopleRemark": "",
    "isAbroadGat": "1",
    "abroadGatRemark": "",
    "address": "江苏省常州市武进区", // 地址
    "addressShen": "江苏省", // 省
    "addressShi": "常州市",  // 市
    "addressXian": "武进区", // 县/区
    "coordinate": "119.83168806623213,31.71513305947064", // 经纬度 此为西太湖校区 建议在区间内随机
    "userId": "uid", // uid 抓包可得， 也可通过查询接口遍历， 根据班号推断（id自增，班级内按学号升序）
    "userJob": "4" 
}
```
+ 正确响应:
  + `{"data":null,"resp_code":0,"resp_msg":"填报成功！"}`

### 查询当日打卡结果接口

+ url: `http://yuyue.cczu.edu.cn:8081/api/healthReporting`
+ method: `GET`
+ query_str: `userId` 用户ID， 抓包得， 非学号。

### 脚本
> 依赖库: `requests`

[多人脚本](health_report.py) 含数据随机函数， 需要重写`get_user` 方法， 部分参数为机器人通知需要，表单内不要

[单人脚本](one.py) 可结合多人脚本的随机温度、随机经纬度方法使用

[查询结果脚本](query_result.py) 查询当日上报结果

