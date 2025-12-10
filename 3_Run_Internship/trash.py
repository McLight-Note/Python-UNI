class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        sorted_nums = sorted(freq, key=lambda x: freq[x], reverse=True)
        return sorted_nums[:k]

print(Solution().topKFrequent([1,2,2,3,3,3], 2))