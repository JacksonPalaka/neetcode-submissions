class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            if i in res.keys():
                res[i]+=1
            else:
                res[i] = 1

        max_nums = dict(sorted(res.items(), key=lambda item: item[1], reverse = True))
        return list(max_nums.keys())[:k]