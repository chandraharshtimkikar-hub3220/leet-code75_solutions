class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0

        while left < right:
            # width is the distance between indices
            width = right - left
            # current water bounded by the shorter line
            current_water = min(height[left], height[right]) * width 
            max_water = max(max_water, current_water)

            #move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1 
        
        return max_water