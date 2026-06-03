class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        s = 0
        e = 0
        count_0 = 0
        max_len = 0
        n = len(nums)

        while e < n:
            if nums[e] == 0:
                count_0 += 1

            while count_0 > k and s<=e:
                if nums[s] == 0:
                    count_0 -= 1
                s+=1

            cur_len = e - s + 1
            max_len = max(cur_len,max_len)

            e += 1

        return max_len