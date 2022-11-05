# question
# 946. Validate Stack Sequences
# https://leetcode.com/problems/validate-stack-sequences/
class Solution:
  def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    stack = []
    i = 0  # popped's index

    for x in pushed:
      stack.append(x)
      while stack and stack[-1] == popped[i]:
        stack.pop()
        i += 1

    return not stack
