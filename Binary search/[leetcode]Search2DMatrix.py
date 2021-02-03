class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = [ i for x in matrix for i in x]
        if target in l:
            return True
        else:
            return False