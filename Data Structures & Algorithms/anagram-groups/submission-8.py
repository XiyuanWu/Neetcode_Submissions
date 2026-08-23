class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for ch in strs:
            key = str(sorted(ch))

            if key not in dic:
                dic[key] = []

            dic[key].append(ch)

        return list(dic.values())