import random

def aaa_phone():
    random_shuzi = random.randint(10000, 99999)  # 随机数用来生成随机电话号码
    a = "182" + str(random_shuzi) + "769"
    return a



def register():
    global kefu_phone

    kefu_phone = aaa_phone()
    kefu_jinli_phone = aaa_phone()
    gcs_phone = aaa_phone()
    fff_phone = aaa_phone()


print(kefu_phone)


