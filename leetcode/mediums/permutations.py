from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def backtrack(current):
            if len(current) == len(nums):
                result.append(current[:])
        
            for i in range(len(nums)):
                if nums[i] in current:
                    continue
                else:
                    current.append(nums[i])
                backtrack(current)
                current.pop()
        
        backtrack([])
        return result
    
# i realized using list checking is not optimal here so im gonna try a different way

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        visited = set()

        def backtrack(current):
            if len(current) == len(nums):
                result.append(current[:])
        
            for i in range(len(nums)):
                if i in visited:
                    continue
                else:
                    current.append(nums[i])
                    visited.add(i) # track indices used in the current depth so for this unique path
                backtrack(current)
                current.pop()
                visited.remove(i) # when going to a different branch remove, same as current
        
        backtrack([])
        return result
    
# this is a little more effiicient cause the check is O(1) instead of O(n)