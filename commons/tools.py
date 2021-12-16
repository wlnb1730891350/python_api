"""
============================
Author:向飞
Time:2020/12/26 11:07
E-mail:947985203@qq.com
============================

"""
import re
import random
import string
from commons.handle_config import conf

# search：匹配到返回一个对象，没有匹配到返回None
# def replace_data(data,cls):
#     '''
#     替换数据
#     :param data: 要进行替换的用例数据（字符串）
#     :param cls: 测试类
#     :return:
#     '''
#     while re.search('#(.+?)#',data):
#         res = re.search('#(.+?)#', data)
#         item=res.group()
#         attr=res.group(1)
#         value=getattr(cls,attr)
#         # 进行替换
#         data=data.replace(item,str(value))
#     return data
#------------------升级版 替换数据同时可以去找测试类或配置文件中匹配-------------
def replace_data(data,cls):
    '''
    替换数据
    :param data: 要进行替换的用例数据（字符串）
    :param cls: 测试类
    :return:
    '''
    while re.search('#(.+?)#',data):
        res = re.search('#(.+?)#', data)
        item=res.group()
        attr=res.group(1)
        try:
            value=getattr(cls,attr)
        except AttributeError:
            value = conf.get('test_data',attr)
        # 进行替换
        data=data.replace(item,str(value))
    return data

# 封装成员断言函数
def assertDictIn(excepted, res):
    '''字典成员运算的逻辑'''
    for k, v in excepted.items():
        if res.get(k) != None and res.get(k) == v:
            print(k, v, 'res中找到了这个键和值')
            pass
        else:
            raise AssertionError('{}[k,v] not in {}'.format(excepted, res))
# 随机生成6到20位包含大小写字母加数字的字符串
def Creat_name():
    i = random.randint(6, 20)
    username = ''.join(random.sample(string.ascii_letters + string.digits, i))
    return username


# 随机生成手机号
def Create_number():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
               "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
               "185", "187", "188", "189"]
    phone = random.choice(prelist) + ''.join(random.choice('0123456789') for i in range(8))
    return phone


# 随机生成邮箱
def Create_email():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
               "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
               "185", "187", "188", "189"]
    num = random.choice(prelist) + ''.join(random.choice('0123456789') for i in range(5))
    pre1 = ['@qq.com', "@163.com"]
    emali=str(num)+''.join(random.choice(pre1))
    print(emali)
    return emali

# 生成包含n个随机字符的字符串
def Create_str(n):
    x = string.ascii_letters + string.digits
    str = ''.join([random.choice(x) for i in range(n)] )
    return str

# s=Create_str(50)
# print(s)
Create_email()