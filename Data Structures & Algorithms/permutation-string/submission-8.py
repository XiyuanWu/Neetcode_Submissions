class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = defaultdict(int)
        count2 = defaultdict(int)

        for i in s1:
            count1[i] += 1

        l = 0
        for r in range(len(s2)):
            
            while r - l + 1 > len(s1):
                count2[s2[l]] -= 1
                if count2[s2[l]] == 0: del count2[s2[l]]
                l += 1

            count2[s2[r]] += 1

            if count1 == count2:
                return True
        return False