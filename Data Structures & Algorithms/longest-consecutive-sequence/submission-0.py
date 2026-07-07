class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lenCounter = 1

        # convert list to a set
        newSet = set(nums)

        maxCount = 0

        # loop through nums
        for num in nums:
            temp = num
            
            while temp-1 in newSet:
                lenCounter += 1
                temp -= 1
            
            if maxCount < lenCounter:
                maxCount = lenCounter

            lenCounter=1
        
        return maxCount