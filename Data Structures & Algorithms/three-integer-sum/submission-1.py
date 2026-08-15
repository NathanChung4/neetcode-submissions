class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()

        for key, val in enumerate(nums):
            if key > 0 and nums[key-1] == nums[key]:
                continue

            l = key+1
            r = len(nums)-1

            while l < r:
                three_sum = val + nums[l] + nums[r]

                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        
        return res