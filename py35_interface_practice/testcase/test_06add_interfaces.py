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
from commons.tools import replace_data
@ddt
class TestAddProject(unittest.TestCase,BaseTest):
    excel = HandleExcel(os.path.join(DATAS_DIR, 'apicases.xlsx'), 'add_interfaces')
    cases = excel.read_data()
    @classmethod
    def setUpClass(cls) -> None:
        cls.user_login()
        cls.add_project()

    @list_data(cases)
    def test_add(self,item):
        # 1、准备数据
        url=conf.get('env','base_url')+item['url']
        headers=self.headers
        item['data']=replace_data(item['data'],TestAddProject)
        params=eval(item['data'])
        method=item['method'].lower()
        expected=eval(item['expected'])
        if item['check_sql']:
            sql = "SELECT * FROM test.tb_interfaces WHERE project_id='{}'".format(params.get('project_id', ''))
            start_count = db2.find_count(sql)
        # 2、请求接口
        response=requests.request(method=method,url=url,json=params,headers=headers)
        res=response.json()
        code=response.status_code
        print('请求参数：', params)
        print('预期结果：', expected)
        print('实际结果',list(res.values())[0])
        print('返回码：', code)
        if item['check_sql']:
            sql="SELECT * FROM test.tb_interfaces WHERE project_id='{}'".format(params.get('project_id',''))
            end_count=db2.find_count(sql)
        # 3、断言
        try:
            if item['check_sql']:
                self.assertEqual(expected['code'],code)
                self.assertEqual(end_count-start_count,1)
            else:
                self.assertEqual(expected['code'],code)
                self.assertIn(str(expected['msg'][0]),str(list(res.values())[0]))
        except AssertionError as e:
            log.error('用例-----【{}】-----执行不通过'.format(item['title']))
            log.exception(e)
            raise e
        else:
            log.info('用例-----【{}】------执行通过'.format(item['title']))



