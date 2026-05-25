class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        k = []
        for i in range(0, len(nums)):
            s = 1
            for j in range(0, len(nums)):
                if j!=i:
                    s*=nums[j]
            k.append(s)
        return k