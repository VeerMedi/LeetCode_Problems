class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        '''maxfreq = max(nums.count(x) for x in nums)
        return sum(nums.count(x) for x in set(nums) if nums.count(x) == maxfreq)
        '''
        freq = Counter(nums)
        maxfreq = max(freq.values())
        return sum(x for x in freq.values() if x == maxfreq)

