from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = -1
        counts = Counter(arr)

        for i in arr:
            if counts[i] == i:
                lucky = max(lucky, i)
        return lucky
        