class Solution(object):
    def merge(self, intervals):
        if len(intervals)<=1:
            return intervals
        def criteria(i):
            return i[0]
        intervals.sort(key=criteria)
        output=[intervals[0]]
        for interval in intervals[1:]:
            if interval[0]<=output[-1][1]:
                output[-1][1]=max(interval[1],output[-1][1])
            else: output.append(interval)
        return output
