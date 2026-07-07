class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key: num, value: index
        newMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in newMap:
                return [newMap[diff], i]
            newMap[n] = i 
        
        # "3": 0
        #
