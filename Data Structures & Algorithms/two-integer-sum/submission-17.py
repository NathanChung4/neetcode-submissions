class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # need to use a hashmap where the indices are the values
        seen = {}   # {value : index}

        for i, v in enumerate(nums):
            diff = target - v
            if diff in seen:
                return [seen[diff], i]
            seen[v] = i
        