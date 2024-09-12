class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)

        # when in doubt do the reverse (increment/decrement)
        res = len(words)

        for w in words:
            for c in w:
                if c not in allowed:
                    res -= 1
                    break

        return res