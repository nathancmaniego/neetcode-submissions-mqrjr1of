class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                if height[l] > leftMax:
                    leftMax = height[l]
                else:
                    res += leftMax - height[l]
                
            else:
                r -= 1
                if height[r] > rightMax:
                    rightMax = height[r]
                else:
                    res += rightMax - height[r]
        return res
                