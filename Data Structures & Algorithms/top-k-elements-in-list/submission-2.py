class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        res = []

        # loop through nums and fill hashmap
        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        # need to use count as index and number as value
        newArray = [[] for _ in range(len(nums) + 1)]

        # fill array
        for i, v in counter.items():
            newArray[v].append(i)
        
        # loop through in reverse and fill res
        for i in range(len(newArray)-1, -1, -1):
            for j in newArray[i]:
                if len(res) == k:
                    return res
                res.append(j)
        
        return res
    