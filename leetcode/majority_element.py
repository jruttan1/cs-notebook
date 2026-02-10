class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
# Keep a current candidate for majority element and a count of how many other elements match it
        for num in nums: 
            if count == 0: # when count is 0 you must set a new candidate
                candidate = num
                count = 1
            elif num == candidate: # if the current number is the same it will reinforce the majority
                count += 1
            else:
                count +- 1 # otherwise it will detract from the majority
        return candidate

# I actually despise this qustion and it made me feel very stupid. 