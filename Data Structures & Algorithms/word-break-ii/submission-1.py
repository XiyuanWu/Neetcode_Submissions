class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        path = []
        result = []

        def dfs(i):
            if i == len(s):
                result.append(" ".join(path))
                return

            for j in range(i, len(s)):
                w = s[i:j+1]
                if w in wordDict:
                    path.append(w)
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return result