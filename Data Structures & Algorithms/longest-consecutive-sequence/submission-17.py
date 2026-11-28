class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        longest = 0

        seen = set(nums)
        for i in nums:
            if i - 1 not in seen:
                curr = 1
                while i + curr in seen:
                    curr += 1
                longest = max(longest, curr)

        return longest
