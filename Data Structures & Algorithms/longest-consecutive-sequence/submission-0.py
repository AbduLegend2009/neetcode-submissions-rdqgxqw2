class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        
        cur = 1
        m = 0

        for i in nums:
            if i - 1 not in nums:
                gap = 1
                while i + gap in nums:
                    cur+=1
                    gap+=1
                if cur > m:
                    m = cur
                cur = 1
        return m