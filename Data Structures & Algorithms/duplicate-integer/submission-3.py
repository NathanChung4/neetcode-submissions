class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # need to use a set for o(1) lookup time
        newSet = set()

        for n in nums:
            if n in newSet:
                return True
            newSet.add(n)
        
        return False