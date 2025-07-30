
# Day 26: Segment Tree for Range Minimum Query (RMQ)

import math

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        x = (math.ceil(math.log2(self.n)))
        max_size = 2 * (2 ** x) - 1
        self.tree = [math.inf] * max_size
        self._build(arr, 0, self.n - 1, 0)

    def _build(self, arr, ss, se, si):
        if ss == se:
            self.tree[si] = arr[ss]
            return arr[ss]
        mid = (ss + se) // 2
        self.tree[si] = min(
            self._build(arr, ss, mid, si * 2 + 1),
            self._build(arr, mid + 1, se, si * 2 + 2)
        )
        return self.tree[si]

    def range_min_query(self, qs, qe):
        return self._query(0, self.n - 1, qs, qe, 0)

    def _query(self, ss, se, qs, qe, si):
        if qs <= ss and qe >= se:
            return self.tree[si]
        if se < qs or ss > qe:
            return math.inf
        mid = (ss + se) // 2
        return min(
            self._query(ss, mid, qs, qe, 2 * si + 1),
            self._query(mid + 1, se, qs, qe, 2 * si + 2)
        )

# Example usage
arr = [1, 3, 2, 7, 9, 11]
seg_tree = SegmentTree(arr)
print("Minimum value in range(1, 5):", seg_tree.range_min_query(1, 5))
