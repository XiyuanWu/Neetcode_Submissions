class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for ch in strs[1:]:
            while not ch.startswith(prefix):
                prefix = prefix[:-1]

        return prefix