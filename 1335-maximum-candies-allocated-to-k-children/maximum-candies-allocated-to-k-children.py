class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Pen & Paper 
            # Our goal is to: find the way we can split up all the piles and assign each children a pile s.t they each have the same number of candies and we maximize the number of candies each child gets 
            # we are actually constrained by the lowest pile right: 
                # whatever is our smallest pile is the bounding factor for how we can assign our children in the case that k >= len(candies)
            # our range of possible values is ultimately 1 to max(candies)
            # We have c candies that each child can get: 
                # we know that is invalid if we are unable to split any of our piles with this candy 
            # if we split each of our values what is the number of children we can assign 
                # this would be an O(n) * 10**5 * 10**3 
            # So this seems entirely in range 

            # [5,8,6], k = 3 
            # range would be l = 1, r = 6 
                # 
        # Bruteforce 
        # Pattern 
            # BOSA
                # TC:O(nlogk)
                # 
        # Implementation Plan 
            # correctness: 
                # we do sum[i]//c
                # then we will do this for the entire list then check if it is true or false at the end 
            # we will do binary searhc to check the values 

        def correctness(i): 
            how_many_kids = 0 
            for a in candies: 
                how_many_kids+=(a//i)
            return how_many_kids >= k 
        l = 0
        r = max(candies)
        while l < r: 
            potential_candies = (ceil((r-l) / 2)) + l 
            if correctness(potential_candies): 
                l = potential_candies 
            else: 
                r = potential_candies - 1 
        return l 
