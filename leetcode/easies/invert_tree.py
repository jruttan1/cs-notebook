class Solution(object):
    def invertTree(self, root):

        if root is None: # Base case if current node is null
            return None # Return None because there is nothing here

        temp = root.left 
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left) 
        self.invertTree(root.right)

        return root 
    
'''
This one was light work once i realized how trees work in Python
'''