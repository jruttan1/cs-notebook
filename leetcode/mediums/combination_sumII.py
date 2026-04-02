from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # the problem here is that if theres 2 of the same element in the input, you can use them each but you cant use the same answer twice

        result = []

        candidates.sort() # sort list to dedupe

        def backtrack(index, current):
            if sum(current) == target:
                result.append(current[:])
            if sum(current) > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]: # i==index means its the first node of this level, so its always valid
                # the second check checks if a node on this level has used the same starting value, so it would have a duplicate result
                    continue
                current.append(candidates[i])
                backtrack(i+1, current) # move to next candidate
                current.pop()

        backtrack(0,[])

        return result
    
# definitely much harder than combo sum 1 but the duplicate guard is intuitive if you think of it as a tree.
# a solution should never start with the same element, cause that would mean its gonna generate duplicate leaves, valid unique combos with be explored with subtrees of that element
# the i > index guard is also confusing but it just checks if where you are in the list is not the first time youve been there, ie first node of this level of the tree.