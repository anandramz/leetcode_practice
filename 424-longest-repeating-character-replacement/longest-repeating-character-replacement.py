class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Pen & Paper 
            # "AABAKABBA", k = 2
            # current streak
            # so we maintain what are the current characters in our hashmap and if we can replace them or not for our max character if we cannot then we contrain the hashmap untill we can 
        # Bruteforce 
        # Pattern 
        # Implementation Plan 
        l = 0 
        map = defaultdict(int)
        max_value = 0
        for r in range(len(s)):
            map[s[r]]+=1
            while ((r-l+1) - max(map.values())) > k:
                map[s[l]]-=1
                l+=1
            max_value = max(r-l+1,max_value)
        return max_value