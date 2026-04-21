class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_len = 0

        for i in seen:
            if i - 1 not in seen:
                current = i
                length = 1

                while current + 1 in seen:
                    current += 1
                    length += 1

                max_len = max(max_len,length)
        return max_len