class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""

        for i in s:
            if i.isalnum():
                clean += i.lower()

        return clean == clean[::-1]