
class Solution:

    def __init__(self, w: list[int]):
        self.cdf = [0] * (len(w) + 1)
        sumL = sum(w)
        cummulative_weight = 0 
        for i in range(len(w)):
            cummulative_weight+=w[i]/sumL
            self.cdf[i+1]+=cummulative_weight

    def pickIndex(self) -> int:
        target = random.random() # samples from U(0,1)
        l = 1 
        r = len(self.cdf) - 1 
        while l < r: 
            m = (l+r)//2
            if self.cdf[m] <= target:
                l = m + 1   
            else:
                r = m
        return r - 1
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
