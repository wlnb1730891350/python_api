"""
============================
Author:向飞
Time:2021/1/17 21:51
E-mail:947985203@qq.com
============================
"""
import os
import requests
import unittest
from commons.handle_excel import HandleExcel
from commons.handle_path import DATAS_DIR
from commons.handle_config import conf
from unittestreport import ddt,list_data
from commons.handle_log import log
from commons.tools import replace_data,Creat_name,Create_email
from commons.handle_mysql import db2

@ddt
class TestRegister(unittest.TestCase):
    excel=HandleExcel(os.path.join(DATAS_DIR,'apicases.xlsx'),'register')
    cases=excel.read_data()
    base_url=conf.get('env','base_url')
    @list_data(cases)
    def test_register(self,item):
        # 1、准备数据
        url=self.base_url+item['url']
        if '#username#' in item['data']:
            setattr(TestRegister,'username',Creat_name())
        if '#email#' in item['data']:
            setattr(TestRegister,'email',Create_email())
        item['data']=replace_data(item['data'],TestRegister)
        params=eval(item['data'])
        method=item['method'].lower()
        expected = eval(item['expected'])
        # 2、请求接口
        response=requests.request(method=method,url=url,json=params)
        res=response.json()
        code=response.status_code
        print('请求参数：',params)
        print('预期结果：', expected)
        print('实际结果：', res)
        print('返回码：',code)
        if item['check_sql']:
            sql = "SELECT * FROM test.auth_user where username='{}'".format(params.get('username', ''))
            count=db2.find_count(sql)
        # 3、断言
        try:
            if item['title']=='注册成功':
                self.assertEqual(expected['code'], code)
                self.assertEqual(count, 1)
            else:
                self.assertEqual(expected['code'], code)
                self.assertIn(expected['msg'],res.values())
        except AssertionError as e:
            log.error('用例-----【{}】-----执行不通过'.format(item['title']))
            log.exception(e)
            raise e
        else:
            log.info('用例-----【{}】------执行通过'.format(item['title']))


