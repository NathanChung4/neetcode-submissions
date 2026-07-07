class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_S, map_T = {}, {}

        # add the key value pairs into the hash map
        for i in range(len(s)):
            map_S[s[i]] = 1 + map_S.get(s[i], 0)
            map_T[t[i]] = 1 + map_T.get(t[i], 0)

        for key in map_S:
            if map_S[key] != map_T.get(key, 0):
                return False
        return True

        