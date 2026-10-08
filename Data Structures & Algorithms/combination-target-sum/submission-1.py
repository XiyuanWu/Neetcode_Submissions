class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def dfs(i, total):
            if total == target: 
                result.append(path.copy())
                return

            if i == len(nums) or total > target:
                return

            # take it
            path.append(nums[i])
            dfs(i, total + nums[i])
            path.pop()

            # skip it
            dfs(i+1, total)

        dfs(0, 0)
        return result