class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        mapTo = {"]" : "[", "}" : "{", ")" : "("}

        for c in s:
            if stack and c in mapTo and stack[-1] == mapTo[c]:
                stack.pop()
            
            else:
                stack.append(c)
        
        if stack:
            return False
        else:
            return True