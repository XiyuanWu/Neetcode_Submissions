class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""

        for ch in s:
            if ch.isalnum():
                result += ch.lower()

        i, j = 0, len(result) - 1

        while i < j:
            if result[i] != result[j]:
                return False

            i += 1
            j -= 1

        return True