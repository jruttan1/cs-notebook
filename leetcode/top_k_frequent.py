class Solution(object):
    def topKFrequent(self, nums, k):
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1

        # build a list of [number, frequency]

        freq_list = []
        for num in frequency:
            freq_list.append([frequency[num], num])
        
        freq_list.sort(reverse=True)


        result = []
        for i in range(k):
            result.append(freq_list[i][1])

        return result
# more of an unorthodox way to do this but it makes sense to me