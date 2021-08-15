# -*- coding: utf-8 -*-
# Time       : 2021/7/22 0:41
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
from selenium.common.exceptions import TimeoutException

from src.armour import GeeTest2
from src.config import FULL_IMG_PATH, NOTCH_IMG_PATH, CHROMEDRIVER_PATH
from .demo_base import CatWalk


class GeeTest2Walk(CatWalk):
    def __init__(self, url, silence=False, chromedriver_path=None):
        super(GeeTest2Walk, self).__init__(url=url, silence=silence, chromedriver_path=chromedriver_path)

    def go(self):
        api = self.set_spider_option()
        try:
            while True:
                self.get_html_handle(api, self.register, 15)
                result = GeeTest2(
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


def demo_geetest2(url):
    GeeTest2Walk(
        url=url,
        silence=False,
        chromedriver_path=CHROMEDRIVER_PATH
    ).go()
