class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        path = []

        def dfs():
            if len(path) == len(nums):
                res.add(tuple(path))
                return

            for i in range(len(nums)):
                if i in used:
                    continue

                used.add(i)
                path.append(nums[i])

                dfs()

                path.pop()
                used.remove(i)

        used = set()
        dfs()

        return [list(x) for x in res]