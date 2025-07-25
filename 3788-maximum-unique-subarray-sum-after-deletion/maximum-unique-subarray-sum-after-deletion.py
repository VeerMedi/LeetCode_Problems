class Solution:
    def maxSum(self, nums: List[int]) -> int:
        m = max(nums)
        if m <= 0:
            return m
        return sum(x for x in set(nums) if x > 0)
