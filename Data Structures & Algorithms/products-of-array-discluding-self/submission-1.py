class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
       ans = [1] * len(nums)

       # Prefix Sum (Here ans is behaving as prefix)
       for i in range(1,len(nums)):
            ans[i] = ans[i-1] * nums[i-1]

       # Suffix Sum
       suffix = 1
       for j in range(len(nums)-1,-1,-1):
           ans[j] *= suffix
           suffix *= nums[j]

       return ans