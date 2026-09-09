class Solution:
    def isValid(self, s: str) -> bool:
        # Pen & Paper 
            # 
        # Bruteforce 
        # Pattern 
            # every last opening bracket must be closed first. Thus we can use a stack to determine this 
        # Implementation Plan 
        map = {")":"(","]":"[","}":"{"}
        stack = []
        for a in s: 
            if a in map: 
                if stack and stack[-1] == map[a]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(a)
        if stack:
            return False
        return True