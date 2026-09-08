class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_freq = max(count.values())
        num_max = sum(1 for freq in count.values() if freq == max_freq)

        return max(
            len(tasks),
            (max_freq - 1) * (n + 1) + num_max
        )