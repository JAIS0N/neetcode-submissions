class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True                      # found the whole word
            if not (0 <= r < ROWS) or not (0 <= c < COLS):
                return False                     # out of bounds
            if board[r][c] != word[i]:
                return False                     # wrong letter
            if (r, c) in path:
                return False                     # already used this cell
            path.add((r, c))

            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False    