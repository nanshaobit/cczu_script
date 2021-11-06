## 企业微信 每日健康打卡

[博客 https://blog.nanshaobit.top/105](https://blog.nanshaobit.top/105)
### 仓库
+ [GitHub](https://github.com/nanshaobit/cczu_script/tree/master/wechat_report_temperature)
+ [Gitee](https://gitee.com/nanshaobit/cczu_script/tree/master/wechat_report_temperature)

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
// 2021-11-06 日 更新

{
    "vaccinesState": "2",   // 2021-10-30 新增 未显示 疫苗接种情况 /1否/2是/
    
    "healthState": "1",   // 健康情况 /1正常/2发热/other其他/
    "healthRemark": "", // 健康状况备注 (健康情况 other时必填)
    
    "temperature": "36.4", // 当前体温 建议在区间内随机
    "temperatureState": "1",  // 体温状况：1.正常 2.异常，由前台根据填写值判断>37.3返回2
    
    "isDangerousArea": "1", // 中高风险地区 路过停留接触 /1 否/ other 其他/
    "dangerousAreaRemark": "", // 中高风险地区备注 (中高风险地区 other时必填)
    
    "isDangerousPeople": "1", // 触过疑似或者确诊 /1 否/ other 其他/
    "dangerousPeopleRemark": "", // 触过疑似或者确诊备注 (触过疑似或者确诊 other时必填)
    
    "isAbroadGat": "1", // 境外人员接触  /1 否/ other 其他/
    "abroadGatRemark": "", // // 境外人员接触备注 (境外人员接触 other时必填)
    
    "isInSchool": "1", // 是否在校 /1 是/ 0 否/
    "campus":"",  // 校区选择 (在校为1必填) ['科教城校区', '西太湖校区']
    
    "chengqu": "武进区",// 现居住地 城区选择  ['武进区', '天宁区', '钟楼区', '新北区', '金坛区', '溧阳市', '其他']
    "zhuzhi": "", // 现居住地详细信息 住校人员要填到宿舍号，家庭地址要具体到门牌号，现居住地在本市的请不要重复填写省、市、区信息
    
    "isclose": "0", // 现居住地是否为管控区域 /0 否/1 是/
    
    "sfz": "", // 身份证号
    "dh": "" // 手机号
    
    "address": "江苏省常州市武进区", // 地址
    "addressShen": "江苏省", // 省
    "addressShi": "常州市",  // 市
    "addressXian": "武进区", // 县/区
    "coordinate": "119.83168806623213,31.71513305947064", // 经纬度定位 此为西太湖校区 建议在区间内随机
    "userId": "uid", //用户id(localStorage.getItem('userid')) uid 抓包可得， 也可通过查询接口遍历， 根据班号推断（id自增，班级内按学号升序）
    "userJob": "4" // 填报用户身份(localStorage.getItem('job') 0.其他、1.教师、2.门卫、3.研究生、4.本科生)
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
