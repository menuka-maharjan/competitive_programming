class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x=""
        if not strs:
            return ""
        if(len(strs)==1):
            return strs[0]
        strs.sort()
        for i in range(len(strs[0])):
            if(strs[0][i]==strs[-1][i]):
                x+=strs[0][i]
            else:
                break
        return x

        