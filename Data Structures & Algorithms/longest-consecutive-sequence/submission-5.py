class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #need a set for o(1) lookup time
        nums = set(nums)

        maxLength = 0

        # need an outer loop and inner loop
        for n in nums:
            # start length at 1 and outside inner loop
            length = 1

            # check if n-1 is NOT in set
            if n-1 not in nums:
                while n+1 in nums:
                    length += 1
                    n += 1

            #checks for every n value
            if length > maxLength:
                maxLength = length
        
        return maxLength