
class Solution:
    def merge (self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x:x[0])

        # Step 2: Initialize result with the first intervals
        res = [intervals[0]]

        # Step 3: Iterate over remaining intervals
        for s, e in intervals[1:]:
            last_s, last_e = res[-1]

            # Overlap case
            if s <=last_e:
                res[-1][1] = max(last_e, e)  # merge by extending the end
            else:
                res.append([s, e])           # no overlap, just add it

        return res