# @DateTime     : 2021-10-01 18:41
# @Author       : Nanshao
# @Mail         : Nanshao@n-s.fun
# @Description  :
import random

import requests


class HealthReport:
    def __init__(self):

        self.url = "http://yuyue.cczu.edu.cn:8081/api/healthReporting"
        """
        Username: webApp
        Password: webApp
        """
        self.headers = {
            "Authorization": "Basic d2ViQXBwOndlYkFwcA==",
            "Referer": "http://yuyue.cczu.edu.cn:8090/"
        }

        self.data = {
            "healthState": "1",
            "healthRemark": "",
            "temperatureState": "1",
            "isDangerousArea": "1",
            "dangerousAreaRemark": "",
            "isDangerousPeople": "1",
            "dangerousPeopleRemark": "",
            "isAbroadGat": "1",
            "abroadGatRemark": "",
        }

    def get_random_jwd(self):
        """
        西太湖校区内 随机经纬度
        :return:
        """
        return "{},{}".format(random.uniform(119.830999, 119.834107), random.uniform(31.709172, 31.717343))

    def get_random_c(self):
        """
        36.3-36.7 随机温度
        :return:
        """
        return random.choice([i / 10 + 36 for i in range(3, 7)])

    def get_user(self):
        """
        从数据库取 待打卡列表
        @return: sid, inchool, qq, uid, ujob, addr, sheng, shi, xian, jwd
        sid: 学号 用于机器人通知，表单内不需要
        inchool: 是否在校，表单不需要，若在校，经纬度将在校区内随机
        qq: QQ号， 用户机器人通知，表单内不需要
        """
        pass
        # 具体内容 自定， 获取打卡列表用户参数
        return ()

    def auto_report_health(self):
        #  多个用户 具体参数见 get_user 说明
        for sid, inchool, qq, uid, job, addr, sheng, shi, xian, jwd in self.get_user():
            c = self.get_random_c()
            if inchool == "1":
                self.data["coordinate"] = self.get_random_jwd()
            else:
                self.data["coordinate"] = jwd

            self.data["address"] = addr
            self.data["addressShen"] = sheng
            self.data["addressShi"] = shi
            self.data["addressXian"] = xian
            self.data["userId"] = uid
            self.data["userJob"] = job
            self.data["temperature"] = c

            # resp 成功响应 {"data":null,"resp_code":0,"resp_msg":"填报成功！"}
            response = ""
            try:
                with requests.post(self.url, data=self.data, headers=self.headers, timeout=5) as resp:
                    response = resp.content.decode()
            except Exception as e:
                # 异常处理
                pass
            finally:
                # 数据交给上游 做下一步处理
                yield qq, sid, addr, c, response


if __name__ == '__main__':
    # 初始化类
    t = HealthReport()
    #  多个用户，循环响应到机器人，脚本不需要。
    for i in t.auto_report_health():
        pass
