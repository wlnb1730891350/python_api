"""
============================
Author:向飞
Time:2021/1/18 14:28
E-mail:947985203@qq.com
============================
"""
import unittest
import os
import requests
from unittestreport import ddt,list_data
from commons.handle_excel import HandleExcel
from commons.handle_path import DATAS_DIR
from commons.handle_config import conf
from commons.tools import replace_data
from commons.handle_log import log
@ddt
class TestLogin(unittest.TestCase):
    excel=HandleExcel(os.path.join(DATAS_DIR,'apicases.xlsx'),'login')
    cases=excel.read_data()
    @list_data(cases)
    def test_login(self,item):
        # 1、准备数据
        url=conf.get('env','base_url')+item['url']
        item['data']=replace_data(item['data'],TestLogin)
        params=eval(item['data'])
        method=item['method'].lower()
        expected=eval(item['expected'])
        # 2、请求接口
        response=requests.request(method=method,url=url,json=params)
        res=response.json()
        code = response.status_code
        print('请求参数：', params)
        print('预期结果：', expected)
        print('实际结果：', res)
        print('返回码：', code)
        # 3、断言
        try:
            self.assertEqual(expected['code'],code)
            self.assertIn(expected['msg'],res.values())
        except AssertionError as e:
            log.error('用例-----【{}】-----执行不通过'.format(item['title']))
            log.exception(e)
            raise e
        else:
            log.info('用例-----【{}】------执行通过'.format(item['title']))


