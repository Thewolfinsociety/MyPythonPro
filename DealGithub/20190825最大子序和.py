# _*_ coding:utf-8 _*_

#@Time :2019/8/25 

# @Author : litao

# @File : 20190825最大子序和.py

class Solution:
    def maxSubArray(self, nums):
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            if dp[i - 1] >= 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        print 'dp=',dp
        return max(dp)

s = Solution()
print 'max=', s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])