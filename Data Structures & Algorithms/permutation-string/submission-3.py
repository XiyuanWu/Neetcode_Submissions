class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = sorted(s1)
        window = []

        l = 0
        for r in range(len(s2)):
            window.append(s2[r])

            if r - l + 1 > len(s1):
                window.pop(0)
                
            if len(window) == len(s1) and sorted(window) == target:
                return True

        return False