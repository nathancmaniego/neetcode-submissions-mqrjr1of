class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights) - 1
        res = []
        while (start < end):
            h1 = heights[start]
            h2 = heights[end]
            diff = end - start
            res.append(min(h1, h2)* diff)
            if h1 > h2:
                end -= 1
            else:
                start += 1
        return max(res)