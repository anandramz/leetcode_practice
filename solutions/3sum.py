
# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        rlist = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r: 
                sum = nums[l] + nums[r] + nums[i]
                if sum > 0:
                    r-=1
                elif sum < 0:
                    l+=1
                else: 
                    rlist.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1

        return rlist

