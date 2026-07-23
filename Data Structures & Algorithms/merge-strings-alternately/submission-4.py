class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        min_length = min(len(word1), len(word2))

        for i in range(min_length):
            result += word1[i]
            result += word2[i]

        if word1: result += word1[min_length:]
        if word2: result += word2[min_length:]

        return result