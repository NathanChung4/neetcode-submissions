class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hashmap first
        # {num: occurrence}
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        # construct the list of lists
        # do plus one because range is exclusive
        buckets = [[] for i in range(len(nums) + 1)]

        # add the values from nums into hashmap
        for num, occurence in seen.items():
            buckets[occurence].append(num)
        
        # make an output hashmap
        outputMap = []

        # final block is to loop through buckets and return until you reach the target
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                outputMap.append(num)
            if len(outputMap) == k:
                return outputMap





