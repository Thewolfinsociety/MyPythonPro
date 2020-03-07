#coding:utf-8
'''
窗口题：
模拟点击窗口题
'''

class window:
    def __init__(self):
        self.x1 = 0     # <x1, y1> 左下角坐标
        self.y1 = 0
        self.x2 = 0     # <x2, y2> 右上角坐标
        self.y2 = 0
        self.num = 0    # 编号
class clickxy:
    def __init__(self):
        self.x = 0     # <x, y> 左下角坐标
        self.y = 0

windows = [ window() for i in range(10)]
print 'windows=',windows
order = ['0'] *10    #从顶向下保存窗口次序；
#把数组中第i位元素插入到首位
def insert(m, n):
    if m == -1:
        for i in range(n, 0, -1):
            order[i] = order[i - 1]
        order[0] = -1
        return
    tmp = order[m]
    for i in range(m, 0 , -1):
        order[i] = order[i-1]
    order[0] = tmp
#模拟点击, 依次序判断是否属于某窗口
def click(x, y, n):
    value = -1
    for i in range(0, n):
        if(x>=windows[order[i]].x1 and x<=windows[order[i]].x2
            and y>=windows[order[i]].y1 and y<=windows[order[i]].y2):
            value = i
            break
    insert(value, n)
def main():
    n = int(raw_input('n='))
    clicknum = int(raw_input('clicknum='))

    for i in range(0 ,n):
        windows[i].x1 = int(raw_input('x1='))
        windows[i].y1 = int(raw_input('y1='))
        windows[i].x2 = int(raw_input('x2='))
        windows[i].y2 = int(raw_input('y2='))
        windows[i].num = i +1
        order[i] = n-i-1
    xylist = [clickxy() for i in range(clicknum)]
    for i in range(0 ,clicknum):
        x = 0
        y = 0
        x = int(raw_input('x='))
        y = int(raw_input('y='))
        xylist[i].x = x
        xylist[i].y = y

    for i in range(0, clicknum):
        x = xylist[i].x
        y = xylist[i].y
        print 'x=',x,'y=',y
        click(x, y, n)
        if order[0] ==-1:
            windows[order[0]].num = 'IGNORED'
            print 'IGNORED'
        else:print windows[order[0]].num
