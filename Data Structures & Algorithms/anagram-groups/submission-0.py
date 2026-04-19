class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i in strs:
            if "".join(sorted(i)) in seen:
                seen["".join(sorted(i))].append(i)
            else:
                seen["".join(sorted(i))] = [i]
        return [i for i in seen.values()]