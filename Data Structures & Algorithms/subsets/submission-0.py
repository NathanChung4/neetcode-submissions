class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            

            # base case
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # decision to include nums[i] (go left)
            subset.append(nums[i])
            dfs(i+1)

            # decision to not include nums[i] (go right)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res