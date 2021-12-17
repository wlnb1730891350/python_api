"""
============================
Author:向飞
Time:2020/12/15 16:57
E-mail:947985203@qq.com
============================
"""
import os
# 获取根目录文件
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 获取测试数据文件路径
TESTCASSE_DIR=os.path.join(BASE_DIR,'testcase')
# 获取测试用例文件路径
DATAS_DIR=os.path.join(BASE_DIR,'datas')
# 获取配置文件路径
CONF_DIR=os.path.join(BASE_DIR,'conf')
# 获取测试报告所在文件路径
REPORTS_DIR=os.path.join(BASE_DIR,'reports')
# 获取日志文件所在路径
LOGS_DIR=os.path.join(BASE_DIR,'logs')



