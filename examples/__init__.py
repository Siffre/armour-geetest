# -*- coding: utf-8 -*-
# Time       : 2021/7/22 0:36
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:

from .demo_geetest2 import demo_geetest2, URLS_GT2
from .demo_geetest3 import demo_geetest3, URLS_GT3

__version__ = ['0.1.1']

__all__ = [
    # 使用了对应验证版本的测试站点
    'URLS_GT3', 'URLS_GT2',
    # demo示例
    'demo_geetest2', 'demo_geetest3'
]
