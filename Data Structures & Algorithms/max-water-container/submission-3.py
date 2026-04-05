class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        res = 0
        while (start < end):
            h1 = heights[start]
            h2 = heights[end]
            diff = end - start
            res = max(min(h1, h2)* diff, res)
            if h1 > h2:
                end -= 1
            else:
                start += 1
        return res