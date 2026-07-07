class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # two phases: find meeting point, find cycle entrance

        # phase 1: fast and slow pointers to find meeting point
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # phase 2: find cycle entry index
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow