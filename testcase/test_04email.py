"""
============================
Author:向飞
Time:2021/1/18 15:03
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
from commons.handle_log import log
@ddt
class TestEmail(unittest.TestCase):
    excel = HandleExcel(os.path.join(DATAS_DIR, 'apicases.xlsx'), 'username')
    cases = excel.read_data()
    @list_data(cases)
    def test_emial(self,item):
        # 1、准备数据
        url=conf.get('env','base_url')+item['url']
        method=item['method'].lower()
        expected=eval(item['expected'])
        # 2、请求接口
        response=requests.request(method=method,url=url)
        res=response.json()
        code=response.status_code
        # 3、断言
        try:
            self.assertEqual(expected['code'],code)
            self.assertEqual(expected['count'],res['count'])
        except AssertionError as e:
            log.error('用例-----【{}】-----执行不通过'.format(item['title']))
            log.exception(e)
            raise e
        else:
            log.info('用例-----【{}】------执行通过'.format(item['title']))
