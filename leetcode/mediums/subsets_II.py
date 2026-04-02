from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        results = []
        nums.sort()

        def backtrack(index, current):
            results.append(current[:])
            
            for i in range(index, len(nums)):
                if i>index and nums[i-1] == nums[i]:
                    continue
                else:
                    current.append(nums[i])
                backtrack(i+1, current)
                current.pop()
            
        backtrack(0, [])

        return results
    
# exact same dupe logic as combo sum II on top of subsets with no base case