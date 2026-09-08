class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Pen & Paper 
            # goal: return the maximum amount of water a container can store.
            # find the max (min(end1,end2) * dist(end1,end2))
            # for any value[i]
        # Bruteforce 
        # Pattern 
            # two pointers
                # we can check the max distance between one another 
                # then reduce it for its min
        # Implementation Plan 

        l = 0 
        r = len(height) - 1
        maxl = 0 
        while l < r: 
            value = min(height[l],height[r])
            maxl = max(value*(r-l),maxl)
            if value == height[l]:
                l+=1
            else:
                r-=1
        return maxl