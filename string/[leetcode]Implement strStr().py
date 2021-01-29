class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(haystack.count(needle)>0):
            return haystack.index(needle)
        else:
            return -1