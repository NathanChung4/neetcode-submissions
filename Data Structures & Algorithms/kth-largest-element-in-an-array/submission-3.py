import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.select(nums, 0, len(nums)-1, len(nums) - k)


    def partition(self, nums, left, right) -> int:

        pivot = nums[right]
        low = left              # everything < pivot goes left of low
        mid = left              # scanner
        high = right            # everything > pivot goes right of high

        while mid <= high:
            if nums[mid] < pivot:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] > pivot:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            else:
                mid += 1
        
        return low, high
    
    def select(self, nums, left, right, target) -> int:
        if left == right:
            return nums[left]

        lo, hi = self.partition(nums, left, right)

        if target < lo:
            return self.select(nums, left, lo-1, target)
        elif target > hi:
            return self.select(nums, hi+1, right, target)
        else:
            return nums[target]  # target is inside equal zone
