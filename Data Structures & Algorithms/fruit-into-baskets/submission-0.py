class Solution:
    def totalFruit(self, nums: List[int]) -> int:
        count = defaultdict(int)
        result = 0

        l = 0
        for r in range(len(nums)):
            count[nums[r]] += 1

            while len(count) > 2:
                count[nums[l]] -= 1
                if count[nums[l]] == 0: del count[nums[l]]
                l += 1

            result = max(result, r - l + 1)

        return result
            