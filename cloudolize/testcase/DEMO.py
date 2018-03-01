import random

def aaa_phone():
    random_shuzi = random.randint(10000, 99999)  # 随机数用来生成随机电话号码
    a = "182" + str(random_shuzi) + "769"
    return a

kefu_phone = aaa_phone()
kefu_jinli_phone = aaa_phone()
gcs_phone = aaa_phone()
fff_phone = aaa_phone()

fruits = [[kefu_phone,kefu_jinli_phone,gcs_phone,fff_phone],
          [1,2,3,4],
          ["客户经理","客户主管","工程师","方欣"]]

# 00 01 02 03 10 11 12 13
for dd in range(len(fruits[1])):
    canshu1 = fruits[0][dd]
    canshu2 = fruits[1][dd]
    canshu3 = fruits[2][dd]


    print("canshu1 = ",canshu1)
    print("canshu2 = ", canshu2)
    print("canshu3 = ", canshu3)


