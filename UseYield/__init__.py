# _*_ coding:utf-8 _*_

#@Time :2019/12/22 

# @Author : litao

# @File : __init__.py.py

import threading
from multiprocessing import Process
import time
# 这是装饰函数
def timer(mode):
    def wapper(func):
        def deco(*args, **kwargs):
            type = kwargs.setdefault('type', None)
            t1 = time.time()
            # 这是函数真正执行的地方
            func(*args, **kwargs)
            t2 = time.time()
            # 计算下时长
            cost_time = t2 - t1
            print("{}-{}花费时间：{}秒".format(mode, type,cost_time))
        return deco
    return wapper
# def timer(type):
#     def wapper(*argv, **kwargs):
#         t1 = time.time()
#         # 这是函数真正执行的地方
#         func(*argv, **kwargs)
#         t2 = time.time()
#         # 计算下时长
#         cost_time = t2 - t1
#         print("花费时间：{}秒".format(cost_time))
#     return wapper
#@timer('Sleep')
def want_sleep(sleep_time, type="2"):
    time.sleep(sleep_time)

@timer("【多进程】")
def multi_process(func, type="2"):
    process_list = []
    for x in range(10):
        p = Process(target=func, args=(2,))
        process_list.append(p)
        p.start()
    e = process_list.__len__()

    while True:
        for pr in process_list:
            if not pr.is_alive():
                e -= 1
        if e <= 0:
            break


if __name__ == '__main__':
    print('Hello')
    want_sleep(2)

    multi_process(want_sleep, type="")