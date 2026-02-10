class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums) # make sure to do it in place otherwise extend will return None
        ans = nums
        return ans
# supa easy