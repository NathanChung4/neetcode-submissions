class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create the hashmap and add the values
        # {val: count}
        seen = {}
        for num in nums:
            seen[num] = 1 + seen.get(num, 0)

        # create the buckets
        buckets = [[] for i in range(len(nums) + 1)]

        # add to the buckets
        for key, val in seen.items():
            buckets[val].append(key)

        # loop through the buckets
        outputList = []
        for i in range((len(buckets) - 1), 0, -1):
            for num in buckets[i]:
                outputList.append(num)
            if k == len(outputList):
                return outputList



