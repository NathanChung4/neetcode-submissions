class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Map, s2Map = {}, {}

        l, r = 0, 0

        # map through s1
        for s in s1:
            s1Map[s] = s1Map.get(s, 0) + 1

        
        for r in range(len(s2)):
            s2Map[s2[r]] = s2Map.get(s2[r], 0) + 1
            
            # too big
            if r - l + 1 > len(s1):
                # shrink left
                s2Map[s2[l]] -= 1
                if s2Map[s2[l]] == 0:
                    s2Map.pop(s2[l])
                l += 1

            if r - l + 1 == len(s1):
                if s1Map == s2Map:
                    return True


        return False
            