#!/usr/bin/env python
# encoding: utf-8
'''
@author: willcat
@contact: deamoncao100@gmail.com
@file: debug.py
@time: 2018/9/20 0:49
@desc: 通过命令行模式调试程序
'''

from scrapy.cmdline import execute

import sys
import os

#获取此文件当前目录
print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "quotes"])