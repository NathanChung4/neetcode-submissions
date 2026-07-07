class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        preVal = 1
        for i in range(len(nums)):
            res[i] = preVal
            preVal *= nums[i]
        
        postVal = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postVal
            postVal *= nums[i]

        return(res)
            
        