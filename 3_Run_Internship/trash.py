# class Solution:
#     def topKFrequent(self, nums, k):
#         freq = {}
        
#         for num in nums:
#             if num not in freq:
#                 freq[num] = 0
#             freq[num] += 1


#         sorted_nums = sorted(freq, key=lambda x: freq[x], reverse=True)
#         return sorted_nums[:k]

# print(Solution().topKFrequent([1,2,2,3,3,3], 2))

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n

        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] = right
            right *= nums[i]
        return res

print(Solution().productExceptSelf([1,2,4,6]))