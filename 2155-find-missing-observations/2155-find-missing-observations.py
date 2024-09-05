class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_m = sum(rolls)

        # mean = total / (m + n)
        # mean * (m + n) = total_m + total_n

        total_n = mean * (m + n) - total_m

        if not (n <= total_n <= n * 6):
            return []

        needed = total_n
        ans = [1] * n
        needed -= n

        for i in range(n):
            delta = min(5, needed)
            ans[i] += delta
            needed -= delta

        return ans