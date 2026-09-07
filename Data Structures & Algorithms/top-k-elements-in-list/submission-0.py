class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for x in nums:
            if x not in map:
                map[x] = 1
            else:
                map[x] += 1
        
        topk = sorted(map, key=map.get, reverse=True)[:k]

        return topk