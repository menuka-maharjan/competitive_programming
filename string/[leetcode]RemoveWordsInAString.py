class Solution:
    def reverseWords(self, s: str) -> str:
        l=[i for i in s.split()]
        l.reverse()
        s=' '.join(l)
        return str(s)