class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            value = abs(target-i)
            if value in nums:
                return [nums.index(i),nums.index(value)]