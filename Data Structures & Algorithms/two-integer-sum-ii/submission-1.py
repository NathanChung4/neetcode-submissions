class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # convert to set - idk abt space tho
        # loop through and check if diff in set

    
        for i, num in enumerate(numbers):
            diff = target - num
            if diff != num and diff in numbers:
                return [i+1, numbers.index(diff)+1]
