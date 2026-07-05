class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        result = r

        while l <= r:
            cap = (l + r) // 2

            # compute cap needed
            days_used = 1
            current_load = 0

            for w in weights:
                if current_load + w <= cap:
                    current_load += w
                else:
                    days_used += 1
                    current_load = w

            if days_used <= days:
                result = cap
                r = cap - 1
            else:
                l = cap + 1

        return result