class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                n = min(heights[i], heights[j])
                temp = n * (j - i) 
                if temp > res:
                    res = temp
        return res