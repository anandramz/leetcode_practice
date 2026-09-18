class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # Pen & Paper 
        # Bruteforce 
        # Pattern 
        # Implementation Paln 
        nums.append(float('-inf'))
        nums = [float('-inf')] + nums
        l = 1 
        r = len(nums) - 2
        while l <= r:
            m = (l + r) // 2
            if nums[m-1] < nums[m] and nums[m] > nums[m+1]:
                return (m -1)
            elif nums[m-1] >= nums[m]:
                r = m - 1
            else:
                l = m + 1
        