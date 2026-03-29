class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
        return -1     
    
'''
This one was simple one i realized that i needed to use a two pointer approach to slice the list. This one takes some of the patterns i learned from two pointer and sliding window questions and applies them to a search.
'''