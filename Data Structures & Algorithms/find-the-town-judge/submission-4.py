class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        ongoing = defaultdict(int)

        for a, b in trust:
            ongoing[a] += 1
            incoming[b] += 1

        for i in range(1, n+1):
            if ongoing[i] == 0 and incoming[i] == n - 1:
                return i

        return -1