class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        def sorter(e):
            return int(e)
        
        nums.sort(key=sorter)
        return nums[-(k)]
