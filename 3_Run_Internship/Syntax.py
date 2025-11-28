'''
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
print(Solution().twoSum([7,5,4,2,1], 9))
'''

# Problem - 2
'''
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        original = x
        reversed_num = 0
        
        while x > 0:
            reversed_num = reversed_num * 10
            reversed_num += x % 10 
            x //= 10
        
        return original == reversed_num
    
print(Solution().isPalindrome(12344321))
'''

# Problem-3
'''
class Solution(object):
    def romanToInt(self, s):
        roman_map={
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
            }
        total = 0
        prev_value = 0

        for char in reversed(s):
            value = roman_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value 
        return total
print(Solution().romanToInt('LVIII'))
'''

# Problem - 4
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix

print(Solution().longestCommonPrefix(['flower', 'flight', 'flow']))
print(Solution().longestCommonPrefix(['dog', 'racecar', 'car']))
'''

# Problem - 5
'''
class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return len(stack) == 0
'''

# Problem - 6
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        prev = 0
        count = 0
        max_count = 0
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
            
        return max_count
        
print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(Solution().findMaxConsecutiveOnes([1,0,1,1,0,1]))