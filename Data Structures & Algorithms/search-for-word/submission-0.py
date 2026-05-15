class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False
        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def backtrack(r: int, c: int, index: int) -> bool:
            if index == len(word):
                return True
            
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
        
            for dr, dc in directions:
                if backtrack(r + dr, c + dc, index + 1):
                    return True
                
            board[r][c] = temp
            return False
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True
        return False
        
        