class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []

        def dfs(open, close):
            if len(path) == n * 2:
                result.append("".join(path))
                return

            # try add (
            if open < n:
                path.append("(")
                dfs(open + 1, close)
                path.pop()
            
            # try add )
            if close < open:
                path.append(")")
                dfs(open, close + 1)
                path.pop()

        dfs(0, 0)
        return result