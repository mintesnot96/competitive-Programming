# question
# 342. Power of Four
# https://leetcode.com/problems/power-of-four/
class Solution(object):
    def isPowerOfFour(self, num):
        if num <= 0:
            return False
        rem = 0
        while num > 1 and rem == 0:
            rem = num % 4
            num = num / 4
            if (num < 1 or rem != 0):
                return False
        return True
