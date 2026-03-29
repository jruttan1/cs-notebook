class Solution(object):
    def groupAnagrams(self, strs):

        groups = {}

        for word in strs:
            fingerprint = "".join(sorted(word))
            if fingerprint not in groups:
                groups[fingerprint] = []
            groups[fingerprint].append(word)
        
        return groups.values()