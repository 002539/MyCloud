__author__ = 'FangXin'
import unittest
import requests
import json
from api_suite import test_api
import random

headers = {'content-type': 'application/json'}
random_shuzi = random.randint(10000, 99999)  # 随机数用来生成随机电话号码
random_phone = "182" + str(random_shuzi) + "769"#定义的随机号码

# 构建测试类
class MyTestSuite(unittest.TestCase):
    def setUp(self):
        print("矩阵风暴MOSS（V1.0）接口测试启动 ---")
        pass

    # 注册接口(注册客户经理)
    def test_aemo_registered(self):
        market_random_phone = random_phone
        # 接口异常处理
        try:
            # 传的参数（json格式）
            content = {
                "phone": market_random_phone,
                "name": "py客户经理账号",
                "type": 6
            }
            r = requests.post(test_api.registered_URL, data=json.dumps(content), headers=headers)
            result = r.json()
            print(r.text)
            # 断言判断是否成功
            self.assertEquals(result['status'], "1")
            '''测试验证代码'''
            print("-------------------------客户经理的手机号" + market_random_phone)
        except BaseException as e:
            print("注册接口请求失败")

    # 登录接口
    def test_demo_login(self):
        # 接口异常处理
        try:
            # 传的参数（json格式）
            content = {
                "phone": random_phone,
                "password": "123456",
                "confirm": "true"
            }
            # 登录请求
            r = requests.post(test_api.login_url, data=json.dumps(content), headers=headers)
            result = r.json()
            print(r.text)

            # 断言判断是否成功
            self.assertEquals(result['status'], "1")

            inp_strr = result
            global market_token
            market_token = result['result']['AccessToken']
        except BaseException as e:
            print("登录接口异常")

    # 客户经理创建订单
    def test_eemo_order(self):
        # 接口异常处理
        try:
            # 创建订单传的参数
            content = {
                "province": "广东",
                "city": "东莞",
                "packageids": "1",
                "servicemoney": "22222",
                "setmoney": "223333",
                "validtime": "23",
                "riskmoney": "1231",
                "companyname": "接口测试公司",
                "agentname": "接口测试代理商",
                "agentphone": "15757178235",
                "baraddr": "浙江-杭州市",
                "barname": "接口测试网吧",
                "phone": 123456,
                "seats_apply": "24",
                "name": "接口测试人员",
                "packagenums": "20",
                "firstmoney": "23333",
                "contractmoney": "2333"
            }

            header = {"Authorization": market_token, 'content-type': 'application/json'}
            # print(type(header))

            r = requests.post(test_api.order_url, data=json.dumps(content), headers=header)

            result = r.json()
            print(r.text)

            # 断言判断是否成功
            self.assertEqual(result['status'], "1")
        except BaseException as e:
            print("创建订单接口失败")

    # # 客户主管审核订单
    # def test_femo_maeket_lead_saledAgree(self):
    #     # 接口异常处理机制
    #     try:
    #         # 订单审核参数
    #         count = {
    #             "orderId":"${id}",
    #             "agree":"1",
    #             "remarks":"接口测试通过",
    #             "saleId":"${market_id}"
    #         }

if __name__ == "__main__":
    unittest.main()
