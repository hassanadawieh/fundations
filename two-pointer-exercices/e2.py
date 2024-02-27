'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
 compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

'''
          
def trap(height):
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water_trapped = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water_trapped += left_max - height[left]
            left += 1  # Move the left pointer to the right
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water_trapped += right_max - height[right]
            right -= 1  # Move the right pointer to the left
    
    return water_trapped

print(trap([0,1,0,1,0,1]))




    
