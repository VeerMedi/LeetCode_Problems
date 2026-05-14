class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
        n=max(nums)
        if len(nums)!=n+1:
            return False
        
        if nums.count(n)!=2:
            return False

        return set(nums)==set(range(1,n+1))