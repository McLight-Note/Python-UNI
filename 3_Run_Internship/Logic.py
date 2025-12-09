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
