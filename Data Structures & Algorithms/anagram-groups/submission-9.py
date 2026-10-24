class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for s in strs:
            key = str(sorted(s))

            if key not in dict:
                dict[key] = []

            dict[key].append(s)

        return list(dict.values())