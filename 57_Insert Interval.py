class Solution:
        def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            s, e = newInterval
            left, merge, right = [], [], []
            for x in intervals: 
                if x[0] > e:
                    right.append(x)
                elif x[1] < s:
                    left.append(x)
                else:
                    merge.append(x)
                if merge:
                    s = min(merge[0][0], s)
                    e = max(merge[-1][1], e)
                
            return left + [[s,e]] + right
            
            

