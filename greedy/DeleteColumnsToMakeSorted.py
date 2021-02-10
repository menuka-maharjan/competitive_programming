class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n=len(strs[0])
        l1=[[strs[i][j]for i in range(len(strs))] for j in range(n)]
        c=0
        for x in l1:
            if x!=sorted(x):
                c+=1
        return c