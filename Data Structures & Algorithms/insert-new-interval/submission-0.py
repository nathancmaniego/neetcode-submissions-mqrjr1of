class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 1 3
        #.    7 8
        #.  3 5
        res = []
        for i in range(len(intervals)):
            # non overlap INSERT newInt (newInterval end < interval start)
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # non overlap, process and skip
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # merge
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res

            

