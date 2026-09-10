class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Pen & Paper 
            # For a chunk to be sorted it needs to include the index it is on 
            # Is there an easy way to keep track of what has been done 
            # We can just take the max index of waht we curently have not encountered once we  
            # Ok we can use a hashmap to check whether we have encountered something or not 
            # Then we use a stack to check if we processed it or not 
            # [4,3,2,1,0]
            # map: 1: True, 0: True 
            # Our map keeps track of if we have found a variable or not 
            # Our stack makes sure that we proccess the values in order from start to finish
        # Bruteforce 
        # Pattern 
        # Implementation Plan 
        index_left_to_proccess = [i for i in range(len(arr)-1,-1,-1)]
        encountered = [False] * len(arr)
        partitions = 0
        for i in range(len(arr)):
            a = arr[i]
            encountered[a] = True 
            while index_left_to_proccess and encountered[index_left_to_proccess[-1]]:
                index_left_to_proccess.pop()
            if not index_left_to_proccess or index_left_to_proccess[-1] > i:
                partitions+=1
        return partitions