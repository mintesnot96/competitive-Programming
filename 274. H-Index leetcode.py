# question
# 274. H-Index
# https://leetcode.com/problems/h-index/
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paper = [0] * (n + 1)
        for c in citations:
            paper[min(n, c)] += 1
        s, h = paper[-1], n
        while h > s:
            h -= 1
            s += paper[h]
        return h
