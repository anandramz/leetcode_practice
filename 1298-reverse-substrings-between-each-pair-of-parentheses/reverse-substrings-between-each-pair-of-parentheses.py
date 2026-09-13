class Solution:
    def reverseParentheses(self, s: str) -> str:
        # Pen & Paper 
            # 
        # Bruteforce 
        # Pattern 
            # stack + queue for reversal 
                # stack + operations
            # TC: O(n)
            # SC: O(n)
        # Implementation Plan 
            # initialize a stack and a queue 
            # loop through the string 
                # whenever we encounter ")" then we will start popping from the stack untill we encounter a "("
                    # we will pop into the queue 
                    # then we will simply dequeue untill empty and append that onto the stack to get our reversed value 
            # we will return "".join(stack)
            # stck = [iloveu]
            # queue = [iloveu]
            stack = []
            queue = deque() 
            for a in s: 
                if a == ")":
                    while stack[-1] != "(":
                        queue.append(stack.pop())
                    stack.pop()
                    while queue: 
                        stack.append(queue.popleft())
                else:
                    stack.append(a)
            return "".join(stack)