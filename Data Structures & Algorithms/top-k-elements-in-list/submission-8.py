class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}
        for i in nums:
            if i in counts:
                counts[i]+=1
            else:
                counts[i] = 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in counts.items():
            buckets[value].append(key)
        
        z = 0
        ours = []
        for i in range(len(buckets) - 1, -1, -1):
            if z >= k:
                break
            if buckets[i]:
                for j in buckets[i]:
                    ours.append(j)
                    z+=1
        return ours
