class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        newInt = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if newInt[1] >= intervals[i][0]:
                newInt = [min(newInt[0], intervals[i][0]), max(newInt[1], intervals[i][1])]
            else:
                res.append(newInt)
                newInt = intervals[i]
        res.append(newInt)
        return res
