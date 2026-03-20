class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # this question is worded so dumb, it is asking for the longest sequence consecutive integers located anywhere in the list. 
        # since order doesnt matter in this question, the smartest approach is to use a set
        # if we turn the list into a set in place with set(). then for each element in the set check if it is the beginning of a sequence by scanning for num-1
        # if num-1 doesnt exist we check for num+1 and for each consecutive add 1 to a running count of longest sequence

        hashset = set(nums)

        longest = 0

        for num in hashset:
            curr = 1 # the current number itself counts as a length of 1
            if not (num - 1) in hashset:
                while (num + 1) in hashset:
                    num = num + 1
                    curr += 1

            longest = max(longest, curr)
        
        return longest

