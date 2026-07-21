class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        
        # use floyds approach
        fast, slow = n, n

        string1 = str(n)
        string2 = str(n)

        while fast != 1:
            slow, fast = 0, 0

            for digit in string1:
                slow += self.sumNums(int(digit))
            string1 = str(slow)

            for digit in string2:
                fast += self.sumNums(int(digit))
            string2 = str(fast)
            fast = 0
            for digit in string2:
                fast += self.sumNums(int(digit))
            string2 = str(fast)
                
            if fast == 1 or slow == 1:
                return True
            if slow == fast:
                return False
        

    def sumNums(self, digit: int) -> int:
        result = digit ** 2

        return result