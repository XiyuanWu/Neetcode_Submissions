class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        seen = set(nums)
        curr, longest = 1, 1

        for i in seen:
            if i - 1 not in seen:
                curr = 1

                while i + curr in seen:
                    curr += 1

                longest = max(curr, longest)

        return longest