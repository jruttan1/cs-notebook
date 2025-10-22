class Solution(object):
    def isAnagram(self, s, t):
        s_letters = ""
        for letter in s:
            s_letters + letter

        t_letters = ""
        for letter in t:
            t_letters + letter

        sorted_s = "".join(sorted(s_letters))
        sorted_t = "".join(sorted(t_letters)) # i need to learn how to use .join

        if sorted_s == sorted_t:
            return True
        return False
        # this is my original solution using sorted strings but it is not optimal since it uses O(n) sorting

from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)
# this is a more optimal solution using Counters which build a dictionary counting how many of each character there is