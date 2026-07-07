class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break
            
            m = (l + r) // 2
            # update result with the mid pointer
            res = min(nums[m], res)
            if nums[m] >= nums[l]:
                #search the right sorted array
                l = m + 1
            else:
                #search the left sorted array
                r = m - 1
        return res
                