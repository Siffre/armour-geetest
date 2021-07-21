# -*- coding: utf-8 -*-
# Time       : 2021/7/22 0:42
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
import time

import selenium.webdriver.support.expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import By
from selenium.webdriver.support.wait import WebDriverWait

from src.armour import GeeTest3
from src.config import FULL_IMG_PATH, NOTCH_IMG_PATH, CHROMEDRIVER_PATH
from .demo_base import CatWalk

URLS_GT3 = [
    # 需要流量过墙
    # 'https://www.jssr.vip/auth/register',
    # 国内可访问
    'https://blx.best/auth/register',
    'https://www.ppyun.co/auth/register'
]


class GeeTest3Walk(CatWalk):
    def __init__(self, url, silence=False, chromedriver_path=None):
        super(GeeTest3Walk, self).__init__(url=url, silence=silence, chromedriver_path=chromedriver_path)

    def go(self):
        api = self.set_spider_option()
        try:
            while True:
                # 进入站点
                self.get_html_handle(api, self.register, 15)
                # 模仿某业务中...
                WebDriverWait(api, 15).until(ec.presence_of_element_located((By.CLASS_NAME, "geetest_radar_tip")))
                time.sleep(2)
                # 墙角遇到爱 -> 调用模块
                result = GeeTest3(
                    driver=api,
                    debug=True,
                    full_img_path=FULL_IMG_PATH,
                    notch_img_path=NOTCH_IMG_PATH,
                ).run()
                if not result:
                    continue
                else:
                    break
        except TimeoutException:
            pass
        finally:
            api.quit()


def demo_geetest3():
    import random
    GeeTest3Walk(
        random.choice(URLS_GT3),
        silence=False,
        chromedriver_path=CHROMEDRIVER_PATH
    ).go()
