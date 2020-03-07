# _*_ coding:utf-8 _*_

#@Time :2019/11/30 

# @Author : litao

# @File : __init__.py.py

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel('INFO')
log.debug('HELLO')
a = 10
def clear():
    for key in list(globals().keys()):
        value = globals()[key]
        print (key)
        print(value.__class__.__name__ )
        if callable(value) or value.__class__.__name__ == "module":

            continue

        del globals()[key]
clear()