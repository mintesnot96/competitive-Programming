# question
# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/
class Solution:
    def myPow(self, x, n):

        result = 1
        current = x
        m = -n if n < 0 else n
        while m > 0:
            
            if m & 1:
                result *= current
            current *= current
            m >>= 1

        return 1 / result if n < 0 else result
