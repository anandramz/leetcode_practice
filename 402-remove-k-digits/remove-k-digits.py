class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for a in num:
            while stack and int(stack[-1]) > int(a) and k: 
                stack.pop()
                k-=1
            stack.append(a)
        while stack and k:
            stack.pop()
            k-=1
        i = 0 
        while stack and i < len(stack) and stack[i] == "0":
            i+=1
        return_string = ''.join(stack[i:])
        if return_string == "":
            return "0"
        return return_string

