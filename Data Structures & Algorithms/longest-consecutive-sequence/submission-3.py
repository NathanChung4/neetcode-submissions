class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        maxLength = 0
        for n in nums:
            length = 1
            if n - 1 not in nums:
                
                while n+1 in nums:
                    n = n + 1
                    length += 1
            if length > maxLength:
                maxLength = length

        return maxLength