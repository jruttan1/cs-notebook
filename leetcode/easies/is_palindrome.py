class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "" #initialize empty string
        
        for i in s.lower(): # loop through characters
            if i.isalnum(): # check if character is alphanumeric
                filtered += i # add to string

        first = 0 #initialize pointers
        last = len(filtered) -1 

        while first < last: #two pointer loop condition to end once indexes cross over

            if filtered[first] != filtered[last]: # check if characters are not equal
                return False 

            first += 1 #advance pointers
            last -= 1

        return True 
    
'''
This problem was pretty tough for me because I was struggling to correctly filter out the non alpha characters, going forward i could have done it in place by leaving the string unfiltered and only using the alpha characters in place during the while loop.'''

