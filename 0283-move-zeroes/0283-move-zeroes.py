class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0

        # place all non-zero elements at the beginning 
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        
        # fill the rest of the arry with zeroes
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1