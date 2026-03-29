class Solution(object):
    def isValid(self, s):
        while True:
            next_s = s.replace("()", "").replace("[]", "").replace("{}", "") # remove valid pairs
            if next_s == s: # check if no changes were made
                break
            s = next_s
        return s == "" # true or false
    
class Solution(object):
    def isValid(self, s):
        stack = [] # initialize an empty list to use as a stack
        hashmap = {')': '(', ']': '[', '}': '{'}  # map each closing bracket to its corresponding opening bracket

        for char in s: # iterate over each character in the input string
            if char in hashmap: # if the character is a closing bracket, this only checks keys
                # check if the stack isn’t empty and the top of the stack matches the required opening bracket
                if stack and stack[-1] == hashmap[char]:
                    stack.pop() # if it matches, pop the opening bracket off the stack
                else:
                    return False # if it doesn’t match (or stack is empty), the string is invalid
            else:
                stack.append(char) # if the character is an opening bracket, push it onto the stack
        
        return not stack # if the stack is empty at the end, all brackets matched correctly; otherwise invalid
    
'''
A stack is maintained while scanning each character, when an opening bracket appears, it is pushed onto the stack. For a closing bracket, the top of the stack is checked for the corresponding opener, if it matches, it is popped; otherwise (or if the stack is empty), the string is invalid. After processing every character, the string is valid only if the stack is empty, indicating that every opener found its closer in the correct order. O(n)
'''