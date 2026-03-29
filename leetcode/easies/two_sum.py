class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(len(nums)): # iterate over range(len because we are examining index not values
            for j in range(i+1, len(nums)): # iterate starting after i
                if nums[i] + nums[j] == target: # check if numbers at indices add to target
                    return [i, j] # return array
'''
This is the brute force way of solving where you iterate through each index and then each following index for each index to find 2 numbers at that index which add to the sum. I struggled here because I forgot that it needed to return the index but needed to check the numbers at the index. O(n^2) double for loop is not optimal
'''

class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums): # loop with num and index
            if target - num in hashmap: # check hashmap for compliment of 2sum (target = num1 + num2 -> target - num1 = num2)
                return [hashmap[target - num], i] # return array of index ofvalue that satisfies (if it exists) and current index
            hashmap[num] = i # add num to dictionary at index i (both values available due to enumerate

'''
This solution maps each number we’ve seen to its index in a hashmap, then for every num it checks if the complement (target - num) is already a key. instead of looking for two numbers that add up to target, it finds the exact number needed for each num, and because it’s in a hashmap you already know its index. O(n) loop + O(1) hashmap lookup
'''