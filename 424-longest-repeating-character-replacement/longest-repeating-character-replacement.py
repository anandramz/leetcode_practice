class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        map = defaultdict(int)
        max_value = 0
        max_freq = 0
        for r in range(len(s)):
            map[s[r]]+=1
            max_freq = max(max_freq, map[s[r]])
            while ((r-l+1) - max_freq) > k:
                map[s[l]]-=1
                l+=1
            max_value = max(r-l+1,max_value)
        return max_value