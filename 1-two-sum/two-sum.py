class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, j in enumerate(nums):
            req = target-j

            if req in dict:
                return[dict[req],i]
            dict[j]=i

        return[]