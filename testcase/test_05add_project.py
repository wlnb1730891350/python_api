"""
============================
Author:向飞
Time:2021/1/18 15:40
E-mail:947985203@qq.com
============================
"""
import os
import unittest
import requests
from commons.handle_excel import HandleExcel
from commons.handle_path import DATAS_DIR
from unittestreport import ddt,list_data
from testcase.fixture import BaseTest
from commons.handle_config import conf
from commons.handle_mysql import db2
from commons.handle_log import log
from commons.tools import Creat_name
@ddt
class TestAddProject(unittest.TestCase,BaseTest):
    excel = HandleExcel(os.path.join(DATAS_DIR, 'apicases.xlsx'), 'add')
    cases = excel.read_data()
    @classmethod
    def setUpClass(cls) -> None:
        cls.user_login()

    @list_data(cases)
    def test_add(self,item):
        # 1、准备数据
        url=conf.get('env','base_url')+item['url']
        headers=self.headers
        # 调用随机生成项目名称函数
        name=Creat_name()
        if '#name#' in item['data']:
            item['data']=item['data'].replace('#name#',name)
        params=eval(item['data'])
        method=item['method'].lower()
        expected=eval(item['expected'])
        # 2、请求接口
        response=requests.request(method=method,url=url,json=params,headers=headers)
        res=response.json()
        code=response.status_code
        print('请求参数：', params)
        print('预期结果：', expected)
        print('实际结果：', res)
        print('返回码：', code)
        if item['check_sql']:
            sql="SELECT * FROM test.tb_projects WHERE name='{}'".format(params.get('name',''))
            count=db2.find_count(sql)
        # 3、断言
        try:
            if item['check_sql']:
                self.assertEqual(expected['code'],code)
                self.assertEqual(count,1)
            else:
                self.assertEqual(expected['code'],code)
                self.assertIn(expected['msg'],res.values())
        except AssertionError as e:
            log.error('用例-----【{}】-----执行不通过'.format(item['title']))
            log.exception(e)
            raise e
        else:
            log.info('用例-----【{}】------执行通过'.format(item['title']))



