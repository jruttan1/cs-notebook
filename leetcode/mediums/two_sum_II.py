from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # since the array is sorted, we can remove values from the end f the list from consideration if they are larger than the target
        # we can use a left pointer and right pointer
        # move right pointr when the sum is greater than target, more left pointer when the sum is less than target

        left = 0
        right = len(numbers) - 1

        while left <= right:
            curr = numbers[left] + numbers[right]

            if curr == target:
                return [left+1, right+1]

            if curr > target:
                right -= 1
            
            if curr < target:
                left += 1