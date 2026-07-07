class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()

        def dfs(i, remaining, combination):
            # base cases
            if remaining == 0:
                res.append(combination.copy())
                return
            elif remaining < 0:
                return
            elif i >= len(nums):
                return
            elif nums[i] > remaining:
                return

            # include
            combination.append(nums[i])
            dfs(i, remaining - nums[i], combination)

            # exclude
            combination.pop()
            dfs(i+1, remaining, combination)


        dfs(0, target, subset)
        return res


