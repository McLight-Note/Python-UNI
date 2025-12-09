# Problem - 1

class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit 

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([1,2,3,4,5]))
print(Solution().maxProfit([7,6,4,3,1]))

# Problem - 2

class Solution:
    def validPalindrome(self, s):
        def isval(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isval(left+1, right) | isval(left, right - 1)
        return True

print(Solution().validPalindrome('abc'))
print(Solution().validPalindrome('abcba'))
print(Solution().validPalindrome('abccba'))
print(Solution().validPalindrome('abca')) 

# Problem - 3

class Solution:
    def bina(self, nums):
        empt = []
        value = 0
        for i in nums:
            value = (value * 2 + i) % 5
            empt.append(value == 0)
        return empt
    
print(Solution().bina([0,1,0]))
print(Solution().bina([1,0,0]))
print(Solution().bina([0,1,1]))

# Problem - 4
class Solution:
    def greatestSumDivisible3(self, nums):
        total = sum(nums)
        if total % 3 == 0:
            return total
        
        mod1 = []
        mod2 = []
        for x in nums:
            if x % 3 == 1:
                mod1.append(x)
            elif x % 3 == 2:
                mod2.append(x)
        
        return print(mod1) and print(mod2)

        # result = 0
        
        # if total % 3 == 1:
        #     remove1 = mod1[0] if mod1 else float('inf')
        #     remove2 = sum(mod2[:2]) if len(mod2) >= 2 else float('inf')
        #     result = total - min(remove1, remove2)
        # else:  # total % 3 == 2
        #     remove1 = mod2[0] if mod2 else float('inf')
        #     remove2 = sum(mod1[:2]) if len(mod1) >= 2 else float('inf')
        #     result = total - min(remove1, remove2)
        
        # return result


print(Solution().greatestSumDivisible3([1,2,3,4,5,6]))
print(Solution().greatestSumDivisible3([3,6,1,8]))
print(Solution().greatestSumDivisible3([3,6,1,8,2,2]))