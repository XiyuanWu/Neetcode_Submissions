class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if sum(nums) % 4 != 0: return False

        target = sum(nums) // 4
        sides = [0, 0, 0, 0]
        nums.sort(reverse=True)

        def dfs(i):
            if i == len(nums):
                return True

            for j in range(4):
                if sides[j] + nums[i] <= target:
                    sides[j] += nums[i]

                    if dfs(i + 1): return True

                    sides[j] -= nums[i]

            return False

        return dfs(0)