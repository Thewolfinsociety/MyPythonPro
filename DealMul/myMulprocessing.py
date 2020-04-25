# _*_ coding:utf-8 _*_

#@Time :2020/4/25 

# @Author : litao

# @File : myMulprocessing.py

import multiprocessing
import time

def worker(interval):
    n = 5
    while n > 0:
        print("The time is {0}".format(time.ctime()))
        time.sleep(interval)
        n -= 1

if __name__ == "__main__":
    p = multiprocessing.Process(target = worker, args = (3,))
    p.daemon = True

    p.start()
    print ("p.pid:", p.pid)
    print ("p.name:", p.name)
    print ("p.is_alive:", p.is_alive())
    #p.join()
    print('hello')