# -*- coding: utf-8 -*-
# Time       : 2021/7/22 0:44
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description: 此文件用于存放一个Selenium运行实例
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class CatWalk(object):
    def __init__(self, url, silence=False, chromedriver_path=None):
        """

        :param url: 真实业务中访问的链接，用于启动selenium
        :param silence: 用于控制Selenium的无头模式，此处为了演示滑动过程默认为False。
                - True：静默启动
                - False：显式启动。
        :param chromedriver_path: chromedriver的存储路径
        """
        self.silence = silence
        self.register = url
        self.CHROMEDRIVER_PATH = chromedriver_path if chromedriver_path else "chromedriver"

    def set_spider_option(self) -> Chrome:
        """
        ChromeDriver settings
        @return:
        """

        options = ChromeOptions()

        # 最高权限运行
        options.add_argument('--no-sandbox')

        # 隐身模式
        options.add_argument('-incognito')

        # 无缓存加载
        options.add_argument('--disk-cache-')

        # 设置中文
        options.add_argument('lang=zh_CN.UTF-8')

        # 更换头部
        options.add_argument(f"user-agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             f"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'")

        options.add_argument('--disable-blink-features=AutomationControlled')

        # 静默启动
        if self.silence is True:
            options.add_argument('--headless')

        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        # 高性能启动，禁止图片加载及js动画渲染，加快Selenium页面切换效率
        chrome_pref = {"profile.default_content_settings": {"Images": 2, 'javascript': 2},
                       "profile.managed_default_content_settings": {"Images": 2}}
        options.experimental_options['prefs'] = chrome_pref
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        d_c = DesiredCapabilities.CHROME
        d_c['pageLoadStrategy'] = 'none'

        try:
            _api = Chrome(
                options=options,
                executable_path=self.CHROMEDRIVER_PATH,
                desired_capabilities=d_c
            )
            _api.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {
                  get: () => undefined
                })
              """
            })
            return _api
        except WebDriverException as e:
            if "chromedriver" in str(e):
                print(f">>> CHROMEDRIVER_PATH路径下指定目录下缺少（对应浏览器版本的）chromedriver")
                print(f">>> 请参考./sspanel-geetest/src/config.py的相关注释配置CHROMEDRIVER_PATH，"
                      f"此外，您还可以访问本项目技术文档寻找答案\n"
                      f"https://github.com/QIN2DIM/sspanel-geetest")
                print(f">>> 若以上方式无法帮助到您，请于本项目issue提交您的报错信息\n"
                      f"https://github.com/QIN2DIM/sspanel-geetest/issues")
                exit()

    @staticmethod
    def get_html_handle(api: Chrome, url, wait_seconds: int = 15):
        api.set_page_load_timeout(time_to_wait=wait_seconds)
        api.get(url)

    def go(self):
        """
        demo重写此模块实现示例站点的行为演示
        :return:
        """
