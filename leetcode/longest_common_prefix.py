class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ref = strs[0]
        i = 0
        prefix = ""
        for i in range(len(ref)): # outer loop is index because you check each word at i then move on
            for word in strs[0:]:
                if i > len(word) - 1: # check edge case: return if the index is out of bounds
                    return prefix
                if word[i] != ref[i]:
                    return prefix
            prefix += ref[i] 
        return prefix