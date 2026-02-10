class Solution(object):
    def isPalindrome(self, x):
        x = str(x)

        first = 0
        last = len(x) - 1

        while first < last:
            if x[first] == x[last]:
                first +=1
                last -=1
            else:
                return False
        
        return True
