class Solution:
    def romanToInt(self, s: str) -> int:
        values= {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total=0
        for i in range(len(s)):
            if i>0 and values[s[i]]>values[s[i-1]]:
                total+=values[s[i]]-2*values[s[i-1]]
            else:
                total+=values[s[i]]
        return total