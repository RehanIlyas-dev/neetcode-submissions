class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}
        for idx, num in enumerate(nums):
            compliment = target - num # Optimal Approach [Y=Target-X] in Brute  Force it would be X+Y=Target
            if compliment in HashMap:
                return [HashMap[compliment],idx]
            HashMap[num] = idx
        return []