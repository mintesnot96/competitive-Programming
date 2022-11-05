# question
# 326. Power of Three
# https://leetcode.com/problems/power-of-three/
class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        if n > 1 and n % 3 == 0:
            return self.isPowerOfThree(n/3)
        if n == 1:
            return True
        return False
