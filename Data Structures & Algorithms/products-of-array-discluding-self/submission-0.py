from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_list = []
        for i in range(len(nums)):
            new_list.append(prod(nums[:i]) * prod(nums[i+1:]))
        return new_list