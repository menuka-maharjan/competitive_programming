class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        z=y[::-1]
        if str(x)==z:
            return True
        else:
            return False