class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        # Store numbers and their frequencies in map
        for x in nums:
            map[x] = map.get(x,0) + 1
        
        # Create a bucket of empty lists 
        freq = [[] for _ in range(len(nums)+1)]

        # Fill the bucket
        for key, value in map.items():
            freq[value].append(key)
        
        # loop backward and collect top k values
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res