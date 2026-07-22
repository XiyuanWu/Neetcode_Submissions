class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = defaultdict(int)
        countT = defaultdict(int)

        for ch in s:
            countS[ch] += 1

        for ch in t:
            countT[ch] += 1

        return countS == countT