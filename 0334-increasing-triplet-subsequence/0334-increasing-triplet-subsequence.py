class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        second = float("inf")

        for num in nums:
            if num <= first:
                first = num # Smallest value found so far
            elif num <= second:
                second = num #smallest value greater than first
            else:
                # found a value grater than both first and second
                return True
        return False