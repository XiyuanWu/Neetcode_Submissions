class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for s in strs:
            key = str(sorted(s))

            if key not in result:
                result[key] = []

            result[key].append(s)
        
        return list(result.values())