class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []


        def dfs(i, remaining, combination):
            # base case 1
            if remaining == 0:
                res.append(combination.copy())
                return

            # base case 2
            elif remaining < 0:
                return

            # base case 3:
            elif i >= len(nums):
                return


            # include
            combination.append(nums[i])
            dfs(i, remaining - nums[i], combination)


            # exclude
            combination.pop()
            dfs(i+1, remaining, combination)
    
        dfs(0, target, subset)
        return res




