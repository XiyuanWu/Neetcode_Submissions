class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        buckets = [0] * k

        def dfs(i):
            if i == len(nums):
                return True

            seen = set()
            for j in range(k):
                if buckets[j] in seen:
                    continue
                if buckets[j] + nums[i] > target:
                    continue
                seen.add(buckets[j])
                buckets[j] += nums[i]
                if dfs(i + 1):
                    return True
                buckets[j] -= nums[i]
            return False

        return dfs(0)