class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for r in range(9):
            for c in range(9):
                nums = board[r][c]
                if nums == '.':
                    continue
                if (("row",r,nums) in seen or 
                    ("col",c,nums) in seen or 
                    ("box",r//3,c//3,nums) in seen):
                    return False
                seen.add(("row",r,nums))
                seen.add(("col",c,nums))
                seen.add(("box",r//3,c//3,nums))
        
        return True
