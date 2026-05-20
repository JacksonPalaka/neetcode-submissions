class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            sort = "".join(sorted(i))
            if sort not in res:
                res[sort] = [i]
            else:
                res[sort].append(i)
                
        return list(res.values())