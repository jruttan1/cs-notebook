class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set() # use a set as the window for O(1) lookups
        L = 0 # sliding window starts at index 0

        for R in range(len(nums)): # can use R as the loop variable since were moving it accross the whole list
            if R - L > k: # this checks if the current range is bigger than k
                window.remove(nums[L]) # if it is you remove the leftmost number form the set
                L += 1 # and move L over 1 place
            if nums[R] in window: # check if nums at R is in the window, since the window will always be less than size k, if this is true the answer will be true
                return True
            else:
                window.add(nums[R]) # this would occur if the window was still the correct size but a new number appears
        return False