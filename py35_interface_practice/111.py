"""
============================
Author:向飞
Time:2021/1/18 12:40
E-mail:947985203@qq.com
============================
"""
import random
import string

# 随机生成6到20位包含大小写字母加数字的用户名
def Creat_usernamePwd():
    i = random.randint(6, 20)
    username = ''.join(random.sample(string.ascii_letters + string.digits, i))
    return username

nm=Creat_usernamePwd()
print(nm)

# 随机生成手机号
def Create_number():

    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
               "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
               "185", "187", "188", "189"]
    phone = random.choice(prelist) + ''.join(random.choice('0123456789') for i in range(8))
    return phone
phone=Create_number()
print(phone)

def Create_email():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
               "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
               "185", "187", "188", "189"]
    num = random.choice(prelist) + ''.join(random.choice('0123456789') for i in range(6))
    # 随机邮箱
    pre1 = ['@qq.com', "@163.com"]
    emali=str(num)+''.join(random.choice(pre1))
    return emali
email=Create_email()
print(email)

def a(t=5):
    if t<2:
        return t
    else:
        return a(t-1)+a(t-2)
print(a())