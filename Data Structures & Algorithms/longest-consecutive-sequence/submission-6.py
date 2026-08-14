class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newSet = set(nums)
        longest = 0

        for num in newSet:

            if num - 1 not in newSet:
                current = 1
                current_num = num
                while current_num + 1 in newSet:
                    current += 1
                    current_num += 1
                
                longest = max(longest, current)
        return longest