# _*_ coding:utf-8 _*_

#@Time :2019/11/2 

# @Author : litao

# @File : __init__.py.py
import logging
try:
    import tornado
    import logging
    logging.basicConfig(level="DEBUG")
    # 必须调用getLOgger获得一个loggging对象后，才可以为他设置级别。
    log = logging.getLogger(__name__)
    # logging的属性，propagate，意思是是否消息是否层层上传。
    log.info(log.propagate)
    # 设置logging对象的级别
    #log.setLevel(logging.WARN)

    log.info('123')
except ImportError:
   import os
   os.system('pip install tornado')
   import requests