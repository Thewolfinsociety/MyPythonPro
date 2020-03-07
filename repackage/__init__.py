# _*_ coding:utf-8 _*_

#@Time :2020/2/22 

# @Author : litao

# @File : __init__.py.py

import re
print(re.escape('www.python.org'))
string = re.escape('www.python.org')
print(string.replace('\\',''))