class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        sMap, tMap = {}, {} # {char : count}
        l = 0
        res = float("inf")
        resL, resR = 0, 0

        # fill in t map
        for c in t:
            tMap[c] = tMap.get(c, 0) + 1

        counter = 0
        for r in range(len(s)):
            
            sMap[s[r]] = sMap.get(s[r], 0) + 1

            if s[r] in tMap and sMap[s[r]] == tMap[s[r]]:
                counter += 1

            while counter == len(tMap):
                if res > (r - l + 1):
                    resL, resR = l, r
                    res = r - l + 1
                sMap[s[l]] -= 1 
                
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    counter -= 1
                l += 1
        if res == float("inf"):
            return ""
        else:
            return s[resL : resR + 1]

