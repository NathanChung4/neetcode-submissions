class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        prefix, postfix = 1, 1

        # 1st pass is fill res with prefixes
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        # 2nd pass is in reverse and applying postfix
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res