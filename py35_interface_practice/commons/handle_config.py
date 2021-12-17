"""
============================
Author:向飞
Time:2020/12/11 21:09
E-mail:947985203@qq.com
============================
"""
from configparser import ConfigParser
import os
from commons.handle_path import CONF_DIR

class Config(ConfigParser):
    def __init__(self,conf_file):
        super().__init__()
        self.read(conf_file,encoding='utf-8')

conf=Config(os.path.join(CONF_DIR,'config.ini'))

