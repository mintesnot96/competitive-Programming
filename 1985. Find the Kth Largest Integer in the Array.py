class Solution(object):
    def kthLargestNumber(self, nums, k):

        def sorter(e):
            return int(e)
        
        nums.sort(key=sorter)
        return nums[-(k)]
