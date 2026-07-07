class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        deque = []
        res = []

        for r in range(len(nums)):
            while deque and nums[r] > nums[deque[-1]]:
                deque.pop(-1)
            deque.append(r)

            if deque[0] < l:
                deque.pop(0)
                
        
            if k == (r - l + 1):
                res.append(nums[deque[0]])
                l += 1


        return res