"""
============================
Author:向飞
Time:2021/1/5 20:25
E-mail:947985203@qq.com
============================
"""
import requests
from jsonpath import jsonpath

from commons.handle_config import conf
from commons.handle_sign import HandleSign
from commons.tools import Creat_name

class BaseTest:

    @classmethod
    def user_login(cls):
        url = conf.get('env', 'base_url') + '/user/login/'
        # --------------------用户登录------------------------
        params = {
            'username': conf.get('test_data', 'username'),
            'password': conf.get('test_data', 'password')
        }
        response = requests.post(url=url, json=params)
        res = response.json()
        # 用户登录成功之后提取token
        cls.token = jsonpath(res, '$.token')[0]
        # 保存含有token的请求头为类属性
        headers={'Authorization':'JWT {}'.format(cls.token)}
        cls.headers = headers
        # 提取用户id给新增项目接口使用
        cls.user_id = jsonpath(res, '$.user_id')[0]

    @classmethod
    def add_project(cls):
        '''添加项目'''
        url = conf.get('env', 'base_url') + '/projects/'
        params = {
            "name": Creat_name(),
            "leader": "xiaofeixiang",
            "tester": "某人",
            "programmer": "某人",
            "publish_app": "接口应用",
            "desc": ""
        }
        # 请求项目接口
        response = requests.post(url=url, json=params, headers=cls.headers)
        res = response.json()
        # 第三步: 提取项目id,保存为类属性
        cls.project_id=jsonpath(res,'$.id')[0]

    @classmethod
    def add_interfaces(cls):
        '''添加接口'''
        # 第一步：准备数据
        url = conf.get('env', 'base_url') + '/interfaces/'
        params = {
            "name": Creat_name(),
            "tester": "asdg",
            "project_id": cls.project_id,
            "desc": "这是一个描述2"
        }
        # 第二步：请求项目接口
        response = requests.post(url=url, json=params, headers=cls.headers)
        res=response.json()
        # 第三步: 提取接口id,保存为类属性
        cls.interfaces_id=jsonpath(res,'$.id')[0]


aa=BaseTest
aa.user_login()
aa.add_project()
aa.add_interfaces()
print(aa.project_id,aa.interfaces_id)
