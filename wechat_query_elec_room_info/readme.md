## 企业微信 电费查询脚本

[博客 https://blog.nanshaobit.top/106](https://blog.nanshaobit.top/106)
### 仓库
+ [GitHub](https://github.com/nanshaobit/cczu_script/tree/master/wechat_query_elec_room_info)
+ [Gitee](https://gitee.com/nanshaobit/cczu_script/tree/master/wechat_query_elec_room_info)

> account 为用户id， 可抓包获得（随机也可，存在就行）。
> aid 应用id 两个校区不同

### 获取楼栋接口

+ url: `http://wxxy.cczu.edu.cn/wechat/callinterface/queryElecBuilding.html`
+ method: `POST`
+ data: 具体见 main.py:get_area()

``` json
{
    "aid": area["aid"], // 应用ID
    "account": "100000", // 用户id
    "area": area["value"] // 区域
}
```

+ 数据位置: 返回数据 json["buildingtab"]

### 查询电费接口

+ url: `http://wxxy.cczu.edu.cn/wechat/callinterface/queryElecRoomInfo.html`
+ method: `POST`
+ data: 具体见 main.py:get_data()

``` json
// 除有注释外，其他内容正常情况不需要修改。
{
    "aid": area["aid"], // 应用ID
    "account": "100000", // 用户id
    "area": area["value"] // 区域
    
    "building": str(building), // 楼栋信息
    "floor": '{"floorid":"","floor":""}', // 置空
    "room": f'{{"room":"","roomid":"{rid}"}}'} // 房间id
}
```

+ 数据位置: 返回数据 json["errmsg"] (可能出错, 提示也在该位置，需要判断)

### 脚本

> 依赖库: `requests`

[脚本](main.py) 使用控制台输入方式交互， 可修改为其他方式交互 如:web、机器人
