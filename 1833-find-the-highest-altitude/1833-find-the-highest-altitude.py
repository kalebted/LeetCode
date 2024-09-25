class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        cur = 0
        for i in gain:
            cur += i
            max_alt = max(max_alt, cur)
        return max_alt