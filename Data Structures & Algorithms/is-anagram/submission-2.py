class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # need hashmaps to store counts of each letter for each word
        sMap, tMap = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sMap[s[i]] = sMap.get(s[i], 0) + 1
            tMap[t[i]] = tMap.get(t[i], 0) + 1
        
        return sMap == tMap