class Solution:
    def maxArea(self, height: List[int]) -> int:
        # the max area of a container is the height of the shorter side * the distance between the walls
        # use 2 pointers starting as left and right. distance will be right - left. track a curr_max and a max
        # check widest container by multiplying the shorter of height[left] and height[right] with right - left
        # move pointer at shorter side and then continue checking max(curr_max, global_max) until while loop ends

        left, right = 0, len(height) - 1
        curr_max = 0
        global_max = 0

        while left<right: 
            if height[left] < height[right]: # find which wall is shorter, capping the height of the container
                curr_max = height[left] * (right - left) # set current max to the current area
                left += 1 # since this wall is smaller it is limiting the size of the container so move the pointer
            else: # the case where the other side is smaller just do the same but reversed
                curr_max = height[right] * (right - left) 
                right -= 1

            global_max = max(curr_max, global_max)
        return global_max
    
    