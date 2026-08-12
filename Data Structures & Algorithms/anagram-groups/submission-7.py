from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # need to return a list of lists
        res = []

        anMap = defaultdict(list)
        

        for s in strs:
            # needs to be in outer loop so it creates a new array for   every word
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            anMap[tuple(count)].append(s)
        
        return list(anMap.values())