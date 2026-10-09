class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        path = []

        def dfs(start, total):
            if total == target:
                result.append(path.copy())
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                if total + nums[i] > target:
                    break

                path.append(nums[i])
                dfs(i+1, total + nums[i])
                path.pop()

        dfs(0, 0)
        return result