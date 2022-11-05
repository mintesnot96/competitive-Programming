# question
# 402. Remove K Digits
# https://leetcode.com/problems/remove-k-digits/
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        remain = len(num) - k
        for dig in num:
            while k and stack and stack[-1] > dig:
                stack.pop()
                k -= 1
            stack.append(dig)
        return ''.join(stack[:remain]).lstrip('0') or '0'
