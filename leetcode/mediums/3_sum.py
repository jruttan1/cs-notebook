class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        #this is the worst question ever
        nums.sort()
        solutions = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            while left<right:
                if nums[left] + nums[right] == -nums[i]:
                    solutions.append([nums[i], nums[left], nums[right]])

                    left+=1
                    while left<right and nums[left] == nums[left-1]:
                        left += 1

                    right -= 1 
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1

                
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1

                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1

        return solutions
            
#this was super brutal ngl