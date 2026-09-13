class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Pen & Paper 
            # [21791]
            # [791]
            # [1,4,3]
                # if we find a smaller digit then we can pop it off the sstack 
            # [1,2,1,9]
                # so whenever we find a smaller digit that is closer we greedily pop it off the stack and because we are popping from the MSB it will be smaller thus resulting in the smallest possible integer 
            # the first two digits are all that matter when we remove something 
                # if we remove the first digit then the s.m.d will inherit its place 
                # if we remove the second digit then the m.s.d will inherit its place 
            # whenever we remove a digit all the digits before it keep their value but all the digits after it became a value of (new number) / 10 
            # the basic idea how can we remove teh digits s.t we place the min possible value in the front 
                # and the max possible digits in the back 
            # or have the digits in ascending order 
            # why does this invariant work 
                # because we always want to take a smaller msb and montonically increasing stack maintains that invariant 
        # Bruteforce 
        # Pattern 
        # Implementation Palna

        stack = []
        for a in num:
            while stack and int(stack[-1]) > int(a) and k: 
                stack.pop()
                k-=1
            stack.append(a)
        while stack and k:
            stack.pop()
            k-=1
        return_integer = 0 
        rlist = []
        i = 0 
        while stack and i < len(stack) and stack[i] == "0":
            i+=1
        if not stack or i == len(stack):
            return "0"
        return_string = "".join(stack[i:])
        return return_string

