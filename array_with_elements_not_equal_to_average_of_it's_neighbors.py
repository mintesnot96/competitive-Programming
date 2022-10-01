class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        i = 0
        
        while i < n-1:
            if i%2 == 0 and nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif i%2 == 1 and nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        
            i += 1
        return nums
