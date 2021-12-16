"""
============================
Author:向飞
Time:2020/12/10 21:50
E-mail:947985203@qq.com
============================
"""
import unittest
from unittestreport import TestRunner
import os
from commons.handle_path import REPORTS_DIR,TESTCASSE_DIR
from unittestreport.core.sendEmail import SendEmail

class RunTest:

    def main(self):
        suite=unittest.defaultTestLoader.discover(TESTCASSE_DIR)
        runner=TestRunner(suite,
                          filename="py35.html",
                          report_dir=REPORTS_DIR,
                          title='测试报告',
                          tester='向飞'
                          )
        runner.run()

        # 将测试结果发送到邮箱
        # runner.send_email(host='smtp.qq.com',
        #                   port=465,
        #                   user='947985203@qq.com',
        #                   password='ldclqycwkzmgbbfg',
        #                   to_addrs='947985203@qq.com',
        #                   is_file=True)

        # # 将测试报告发送到钉钉群组
        # webhook=''
        # runner.dingtalk_notice(url=webhook,key='关键字')
#  ------------扩展自定义邮件的标题和内容-------------
# from unittestreport.core.sendEmail import SendEmail
#
# em = SendEmail(host='smtp.qq.com',
#                port=465,
#                user='xiangfei',
#                password='ldclqycwkzmgbbfg')
# em.send_email(subject="测试报告", content='邮件内容', filename=r'D:\python_35_class\py35_23day_project\reports\py35.html', to_addrs='947985203@qq.com')
# # ------------------------------------------------

if __name__ == '__main__':
    test=RunTest()
    test.main()