class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # Pen & Paper 
            # if we dont do any operations our penalty would be max(nums)
            # the minimum possible penalty is 1 
            # thus our range for the penatly is [1,max(nums)), max(nums) is already known 
        # Bruteforce 
        # Pattern 
            # We can reformulate a BOSA: 
                # given we try to get a maximum penalty we will try to look for it 
                # SC: O(1)
                # TC(O(nlogk))
        # Implementation Plan 
            # function:     
                # we loop through the list
                    # either a value is below or above our penalty 
                    # so we divide it by our value to get how many it takes to decrease 
        def function(penalty):
            ops = 0 
            for a in nums:
                if a <= penalty:
                    continue   
                ops+=(ceil(a/penalty)-1)
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