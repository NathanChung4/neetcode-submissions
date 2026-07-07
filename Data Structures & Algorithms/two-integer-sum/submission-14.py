class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        output = []

        if len(nums) == 2:
            output.append(0)
            output.append(1)
            return output

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
                    print(j)
                    return output
            

