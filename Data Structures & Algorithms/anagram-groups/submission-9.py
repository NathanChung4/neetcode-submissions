from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # need to return a list of lists
        res = []
        countMap = defaultdict(list)

        for s in strs:

            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            countMap[tuple(count)].append(s)
        
        for val in countMap.values():
            res.append(val)
        
        return res