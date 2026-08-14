class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # need output list same size as nums
        res = [0] * len(nums)
        # need prefix and postfix
        prefix, postfix = 1, 1

        # first pass is prefix
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # second pass is apply postfix
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res