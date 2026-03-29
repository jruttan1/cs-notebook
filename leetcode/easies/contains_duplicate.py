class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return(True)
            seen.add(num)
        return False
'''
This is the optimal O(n) solution for this problem, since checking if a num is in the set is O(1). 
I originally used a list to store the seen values which let to an non optimal O(n^2) solution.
'''