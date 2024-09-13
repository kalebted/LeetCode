class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        for n in arr:
            prefix.append(prefix[-1] ^ n)
        
        res = []
        for l, r in queries:
            res.append(
                prefix[r + 1] ^ prefix[l]
            )
        return res