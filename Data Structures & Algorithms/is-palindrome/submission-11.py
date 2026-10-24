class Solution:
    def isPalindrome(self, string: str) -> bool:
        result = ""

        for s in string:
            if s.isalnum():
                result += s.lower()

        return result == result[::-1]
