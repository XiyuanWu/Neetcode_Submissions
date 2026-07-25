class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            key = str(sorted(s))

            if key not in group:
                group[key] = []

            group[key].append(s)

        return list(group.values())