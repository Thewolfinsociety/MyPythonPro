# _*_ coding:utf-8 _*_

#@Time :2019/8/24 

# @Author : litao

# @File : 20190824通配符匹配.py
'''
你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        j = 0
        start = -1
        match = 0
        while i < len(s):
            # 一对一匹配,匹配成功一起移
            if j < len(p) and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1
            # 记录p的"*"的位置,还有s的位置
            elif j < len(p) and p[j] == "*":
                start = j
                match = i
                j += 1
            # j 回到 记录的下一个位置
            # match 更新下一个位置
            # 这不代表用*匹配一个字符
            elif start != -1:
                j = start + 1
                match += 1
                i = match
            else:
                return False
         # 将多余的 * 直接匹配空串
        return all(x == "*" for x in p[j:])


s = Solution()
state = s.isMatch("aadfdf", "a*")
print 'ismatch=',state



