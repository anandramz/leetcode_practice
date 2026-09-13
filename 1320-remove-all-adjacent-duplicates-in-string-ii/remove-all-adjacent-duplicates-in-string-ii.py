class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # Pen & Paper 
            # reminds me alot of LIFO 
            # in our stack we can store [chr,count]
                # if the top of the stack is the character that we are appending then we increase the count 
                # else we will just append the character with [chr,1]
        # Bruteforce 
        # Pattern 
            # stack 
                # LIFO 
        # Implementation Plan 
            # TC: O(n)
            # SC: O(n)
            # Edge Cases: 
                # we have any empty stack => "" 
            # initialize a stack 
            # loop through the string 
                # handle appending a character with its count to the stack:
                    # in our stack we can store [chr,count]
                        # if the top of the stack is the character that we are appending then we increase the count 
                        # else we will just append the character with [chr,1]
                # we will pop off the chracter if it equals k 
            # then we will loop through the stack and append the characters to a string as needed 
                # we will append it to a list and then use .join()
        
        stack = []
        for a in s: 
            if stack and stack[-1][0] == a: 
                stack[-1][1]+=1
            else:
                stack.append([a,1])
            while stack and stack[-1][1] == k:
                stack.pop()
            while len(stack) > 2 and stack[-1][0] == stack[-2][0]:
                char, count = stack.pop()
                stack[-1][1]+=count

        rlist = []
        for char, count in stack:
            rlist.append(char * count)
        return "".join(rlist)
