class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = defaultdict(int)
        count2 = defaultdict(int)

        for i in s:
            count1[i] += 1

        for i in t:
            count2[i] += 1

        return count1 == count2