# _*_ coding:utf-8 _*_

#@Time :2020/3/12 

# @Author : litao

# @File : TwoNumberAdd.py

# 两数相加
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode(0)
        l = ret
        while (True):
            if l1 is None and l2 is None:
                break
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            l.val += v1 + v2
            if l.val >= 10:
                l.next = ListNode(1)
                l.val -= 10

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            if l1 is None and l2 is None:
                break
            if l.next is None:
                l.next = ListNode(0)
            l = l.next
        return ret


