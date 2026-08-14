class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1

        while l < r:
            # advance pointers until theyre valid chars
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            # compare the chars
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True