class Solution(object):
    def maxDepth(self, root):
        
        if not root:
            return 0 # return 0 because this node doesnt exist and has no depth
        
        left_depth = self.maxDepth(root.left) # recurse left
        right_depth = self.maxDepth(root.right) # recurse right

        max_depth = max(left_depth, right_depth) # find the maximum depth between left and right subtrees

        return(1 + max_depth) # add one to the max depth of the subtrees to account for the current node
    
'''
This one was actually difficult finding out how to accumulate the depth properly, 
this solution basically works up each subtree adding one for each recursive call, 
ending recursion at base and then computing max between left and right subtrees, 
then adding one for the current node.'''