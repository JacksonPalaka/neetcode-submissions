class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for num in range(len(nums)):
            diff = target - nums[num]
            if diff in seen:
                return [seen[diff],num]
            seen[nums[num]] = num