class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # use 2 pointers starting at min width
        # window size - count of most freq <=k 
        # find most freq char by hashing everything in window as you expand

        left = 0
        counts = {}
        result = 0 

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1 # add each new value to the hashmap\
            most_freq = max(counts.values()) 
            if not right - left + 1 - most_freq <= k: # finding out this formula is the hardest part but you csan construct it from constraints of a valid window
                counts[s[left]] -= 1
                left += 1 # increment if the window is invalid
            result = max(right - left + 1, result)

        return result

# lowkey forgot the sliding window for loop thing but it worked out