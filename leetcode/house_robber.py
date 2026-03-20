class Solution:
    def rob(self, nums: List[int]) -> int:
        # if you rob house i, you didnt rob i-1 and you cant rob i+1
        # modify dp formula based on base cases
        # Base cases are: dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
        # dp[i] = max(dp[i-1], nums[i] + dp[i-2]) 
        # the dp list being built out is the max amt money u can have by that house in the list
        # at each hpuse you take either the previous total (skip), or the total from 2 houses ago and the current which would be robbing the current house

        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) > 1:
            dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1]
# struggled finding the correct base cases and dp formula. next time i need to write out the intuitive process for the decision making process at each index.

