import unittest
import requests
from api_suite import test_api
import json
import random

headers = {'content-type': 'application/json'}

# 简单生成随机电话号码
def random_phone():
    random_shuzi = random.randint(10000, 99999)  # 随机数用来生成随机电话号码
    random_phone = "182" + str(random_shuzi) + "769"
    return random_phone


'''创建各个角色账号，将所有账号在userinfo注册并登录获取其token和id值'''
market_random_phone = random_phone()  # 客户经理账号
market_lead_random_phone = random_phone()  # 销售主管账号
agent_random_phone = random_phone()  # 代理商账号
engineer_random_phone = random_phone()  # 工程师账号
engineer_lead_random_phone = random_phone()  # 技术支持主管账号
visit_random_phone = random_phone()  # 回访员账号
risk_management_random_phone = random_phone()  # 风控账号
ceo_random_phone = random_phone()  # CEO账号
money_random_phone = random_phone()  # 财务账号
supplier_random_phone = random_phone()  # 供应商账号


# 接口请求函数requests_DEMO
def requests_DEMO(DEMO_URL, content, headers):
    global result
    r = requests.post(DEMO_URL, data=json.dumps(content), headers=headers)
    result = r.json()
    print(r.text)
    return

class Mytest(unittest.TestCase):
    def setUp(self):
        print("矩阵风暴MOSS（V1.0）接口测试启动 ---")
        pass

    '''注册所有账号'''
    def test_a_register(self):


        '''将账号，type，名称放在fruits列表里面'''
        fruits = [[market_random_phone, market_lead_random_phone, agent_random_phone, engineer_random_phone,
                   engineer_lead_random_phone,visit_random_phone,risk_management_random_phone,ceo_random_phone,
                   money_random_phone,supplier_random_phone],
                  [6,5,3,11,10,13,8,9,7,12],
                  ["客户经理账号", "销售主管账号", "代理商账号", "工程师账号", "技术支持主管账号", "回访员账号", "风控账号",
                   "CEO账号","财务账号", "供应商账号"]]

        '''创建各个角色的账号'''
        for num in range(len(fruits[1])):
            # 接口异常处理
            try:
                # 传的参数（json格式）
                content = {
                    "phone": fruits[0][num],
                    "name": fruits[2][num],
                    "type": fruits[1][num]
                }
                requests_DEMO(DEMO_URL=test_api.registered_URL, content=content, headers=headers)
                # 断言判断是否成功
                self.assertEquals(result['status'], "1")

            except BaseException as e:
                print("########注册失败########")

     '''登录各个账号，并获取token和userid'''
     # 客户经理登录
     def test_b_login_market(self):
         # 接口异常处理机制
        try:
            # 传的参数
            content = {"phone":market_random_phone,# 客户经理账号
                       "pwd":"123456",# 密码
                       "confirm":"true"}

            requests_DEMO(DEMO_URL=test_api.login_url, content=content, headers=headers)
            # 断言判断是否成功
            self.assertEquals(result['result'], "登录成功")

            # 获取登录token和id
            inp_strr = result
            global market_token
            global market_id
            market_token = result['result']['AccessToken']
            market_id = result['result']['id']

        except BaseException as e:
            print("########客户经理登录失败########")

    # 客户主管登录
    def test_c_login_market_lead(self):
        # 接口异常处理机制
        try:
            # 传的参数
            content = {"phone": market_lead_random_phone,  # 客户主管账号
                       "pwd": "123456",  # 密码
                       "confirm": "true"}

            requests_DEMO(DEMO_URL=test_api.login_url, content=content, headers=headers)
            # 断言判断是否成功
            self.assertEquals(result['result'], "登录成功")

            # 获取登录token和id
            inp_strr = result
            global market_lead_token
            global market_lead_id
            market_lead_token = result['result']['AccessToken']
            market_lead_id = result['result']['id']

        except BaseException as e:
            print("########客户主管登录失败########")

    # 客户经理登录
    def test_c_login_market(self):
        # 接口异常处理机制
        try:
            # 传的参数
            content = {"phone": market_random_phone,  # 客户经理账号
                       "pwd": "123456",  # 密码
                       "confirm": "true"}

            requests_DEMO(DEMO_URL=test_api.login_url, content=content, headers=headers)
            # 断言判断是否成功
            self.assertEquals(result['result'], "登录成功")

            # 获取登录token和id
            global market_token
            global market_id
            market_token = result['result']['AccessToken']
            market_id = result['result']['id']

        except BaseException as e:
            print("########客户经理登录失败########")

    # 代理商登录
    def test_c_login_agent(self):
        # 接口异常处理机制
        try:
            # 传的参数
            content = {"phone": agent_random_phone,  # 代理商账号
                       "pwd": "123456",  # 密码
                       "confirm": "true"}

            requests_DEMO(DEMO_URL=test_api.login_url, content=content, headers=headers)
            # 断言判断是否成功
            self.assertEquals(result['result'], "登录成功")

            # 获取登录token和id
            global agent_token
            global agent_id
            agent_token = result['result']['AccessToken']
            agent_id = result['result']['id']

        except BaseException as e:
            print("########代理商登录失败########")

    # 工程师登录
    def test_c_login_agent(self):
        # 接口异常处理机制
        try:
            # 传的参数
            content = {"phone": agent_random_phone,  # 工程师账号
                       "pwd": "123456",  # 密码
                       "confirm": "true"}

            requests_DEMO(DEMO_URL=test_api.login_url, content=content, headers=headers)
            # 断言判断是否成功
            self.assertEquals(result['result'], "登录成功")

            # 获取登录token和id
            global agent_token
            global agent_id
            agent_token = result['result']['AccessToken']
            agent_id = result['result']['id']

        except BaseException as e:
            print("########工程师登录失败########")


if __name__ == "__main__":
    unittest.main()