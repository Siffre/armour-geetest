# -*- coding: utf-8 -*-
# Time       : 2021/7/22 0:48
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
import os
import time
from os.path import dirname, join, exists
from sys import platform

# ---------------------------------------------------
# TODO (√)CHROMEDRIVER_PATH -- ChromeDriver的路径
#  本项目依赖google-chrome驱动插件，请确保您的开发环境中已经安装chrome以及对应版本的chromedriver
#  本项目预装的chromedriver_win32 版本号为 91.0.4472.101

# 1. 配置google-chrome开发环境
# 1.1 安装Chrome
# 若无特殊需求请直接拉取最近版程序
# >> Windows -> https://www.google.cn/chrome/index.html
# >> Linux -> https://shimo.im/docs/5bqnroJYDbU4rGqy/

# 1.2 安装chromedriver
# 查看chrome版本并安装对应版本的匹配操作系统的chromedriver。
# >> http://npm.taobao.org/mirrors/chromedriver/

# 1.3 配置环境变量
# （1）将下载好的对应版本的chromedriver放到工程`./sspanel-mining/src`目录下
# （2）或配置Chrome环境变量，Windows编辑系统环境变量Path，定位到Application文件夹为止，示例如下：
#      C:\Program Files\Google\Chrome\Application

# 2. 注意事项
#   -- 本项目基于Windows环境开发测试，Linux环境部署运行，若您的系统基于MacOS或其他，请根据报错提示微调启动参数。
#   -- 若您的Chrome安装路径与上文所述不一致，请适当调整。
#   -- 若您不知如何查看Chrome版本或在参考blog后仍遇到预料之外的问题请在issue中留言或通过检索解决。
#       >> Project：https://github.com/QIN2DIM/armour-geetest
# ---------------------------------------------------
if "win" in platform:
    # 定位chromedriver根目录
    CHROMEDRIVER_PATH = dirname(__file__) + "/chromedriver.exe"
    # 定位工程根目录 SERVER_DIR_PROJECT
    SERVER_DIR_PROJECT = dirname(__file__)
else:
    CHROMEDRIVER_PATH = dirname(__file__) + "/chromedriver"
    SERVER_DIR_PROJECT = f"/qinse/sspanel-mining"

# 文件数据库 目录根
DIR_DATABASE = join(SERVER_DIR_PROJECT, "database")
# 拼图缓存路径
DIR_CACHE = join(DIR_DATABASE, "cache")
FULL_IMG_PATH = join(DIR_CACHE, f"full_img_{time.time()}.png")
NOTCH_IMG_PATH = join(DIR_CACHE, f"notch_img_{time.time()}.png")

# 若chromedriver不在CHROMEDRIVER_PATH指定的路径下 尝试从环境变量中查找路径
if not exists(CHROMEDRIVER_PATH):
    CHROMEDRIVER_PATH = None
# 避免因.gitignore造成的目录残缺引发的FileNotFound错误
for _pending in [DIR_DATABASE, DIR_CACHE]:
    if not exists(_pending):
        os.mkdir(_pending)
