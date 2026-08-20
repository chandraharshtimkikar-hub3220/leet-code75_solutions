class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # Step 1: compute prefix products for each element
        prefix = 1
        for i in range (n):
            res[i] = prefix
            prefix *= nums[i]

        #step 2: multiply by suffix products on the fly
        suffix = 1 
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i] 

        return res       
        