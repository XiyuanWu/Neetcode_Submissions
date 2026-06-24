class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for i in strs:
            key = "".join(sorted(i))

            if key not in dic:
                dic[key] = []

            dic[key].append(i)

        return list(dic.values())