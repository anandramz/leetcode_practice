# we are given a list of weights, and we have to design a function that randomly picks an index based off the probability of each weight 
    # weights list are a probability distribution 
# pickIndex called up to 10**4 times 
# multiple answers are allowed however it has to follow the law of large numbers with the probability distribution 
# we cannot have a weight of 0 it always has to be atleast 1 
# [1/4,3/4]




class Solution:

    def __init__(self, w: list[int]):
        self.prefix_map = [0] * (len(w) + 1)
        suml = sum(w)
        self.weights = [a/suml for a in w]
        cummulative_weight = 0 
        for i in range(len(self.weights)):
            cummulative_weight+=self.weights[i]
            self.prefix_map[i+1]+=cummulative_weight

    def pickIndex(self) -> int:
        target = random.random()
        l = 1 
        r = len(self.prefix_map) - 1 
        while l <= r: 
            m = (l+r)//2
            if self.prefix_map[m-1] < target <= self.prefix_map[m]:
                return m - 1
            elif self.prefix_map[m] < target:
                l = m + 1
            else: 
                r = m - 1
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
"""
--- 25-MINUTE INTERVIEW FRAMEWORK ---

1. CLARIFY (0-5m)
   [x ] Restate problem in my own words
   [ x] Identify edge cases (empty, duplicates, bounds)
   [ ] Create 1 custom test case

2. PLAN (5-12m)
   [ x] State the brute force baseline
   [] Brainstorm optimal approaches (Time/Space)
   [] Write a 4-5 line pseudo-code outline

3. IMPLEMENT (12-20m)
   [ ] Code strictly from the outline
   [ ] Use descriptive variable names
   [ ] Talk out loud continuously

4. REVIEW (20-25m)
   [ ] Dry run code against test cases manually
   [ ] Track variable states line-by-line
   [ ] State final Time and Space complexity
-------------------------------------
"""