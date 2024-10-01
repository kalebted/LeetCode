class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        f = collections.Counter(v % k for v in arr)

        for key in f.keys():
            # key is a number between 0 and k - 1 inclusive
            other_key = (k - key) % k

            if key == other_key:
                if f[key] % 2 != 0:
                    return False
            else:
                    if f[key] != f[other_key]:
                        return False
        return True