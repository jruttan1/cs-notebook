from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []

        def backtrack(index, current):
            if sum(current) == target: # base case check for correct cases
                result.append(current[:]) # dupe result to pass value not reference
            if sum(current) > target: # prune branches where proceeding is guarenteed to be wrong
                return

            for i in range(index, len(candidates)): # passing index makes it so u can reuse the current element but not go back
                current.append(candidates[i]) 
                backtrack(i, current)
                current.pop()
        
        backtrack(0, [])
        return result