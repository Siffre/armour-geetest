# -*- coding: utf-8 -*-
# Time       : 2021/7/22 0:36
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description: 一种较高识别率的GeeTest滑动验证解决方案
#   -- [注意] 本测试案例使用的站点需要流量过墙，若条件允许请开启系统代理
#   -- 如何知道更多类似的使用geetest滑动验证的站点？请访问
#   https://github.com/QIN2DIM/sspanel-mining
import random

from examples import demo_geetest2, demo_geetest3

URLS_GT2 = [
    # 需要流量过墙
    'https://xn--9kq568dvkr.com/auth/register',
    'https://unexpecteddomainnamepro.xyz/auth/register',
    # 国内可访问
    # 'https://sopen.xyz/auth/register'
]
URLS_GT3 = [
    # 需要流量过墙
    'https://www.jssr.vip/auth/register',
    'https://blx.best/auth/register',
    'https://www.ppyun.co/auth/register'
    # 国内可访问
    "https://www.kaikaiyun.icu/auth/register",
]

if __name__ == '__main__':
    # 运行GeeTest_v2滑动验证测试案例
    demo_geetest2(random.choice(URLS_GT2))
    # 运行GeeTest_v3滑动验证测试案例
    demo_geetest3(random.choice(URLS_GT3))
