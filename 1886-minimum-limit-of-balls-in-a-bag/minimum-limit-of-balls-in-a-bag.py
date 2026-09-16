class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def function(penalty):
            ops = 0 
            for a in nums:
                if a <= penalty:
                    continue   
                ops+=((ceil(a/penalty)-1))
            return ops <= maxOperations
        
        l = 1
        r = max(nums)
        while l < r: 
            m = (r + l) // 2
            if function(m):
                r = m
            else: 
                l = m + 1
        return r