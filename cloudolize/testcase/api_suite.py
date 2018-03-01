__author__ = 'FangXin'
class test_api(object):
    '''定义所有接口的URL'''
    #IP地址
    URL = "https://cloudolize.cn"

    #注册接口
    registered_URL = URL + "/WeCloud/user/registerTest"

    #登录接口
    login_url = URL + "/WeCloud/user/loginTest"

    #客户经理创建订单
    order_url = URL + "/WeCloud/order"

    #客户主管审核订单
    saledAgree_url = URL + "/WeCloud/order/saledAgree"

    


