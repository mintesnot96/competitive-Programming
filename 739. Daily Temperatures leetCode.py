# question
# https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, T: List[int]):
        stack = []
        ans = [0]*len(T)
        for i,v in enumerate(T):
            while stack and stack[-1][1]<v:
                index,value = stack.pop()
                ans[index] = i-index
            stack.append([i,v])
        return ans
