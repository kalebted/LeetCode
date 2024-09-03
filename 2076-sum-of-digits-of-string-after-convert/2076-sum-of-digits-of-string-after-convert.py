class Solution:
    def getLucky(self, s: str, k: int) -> int:
        mapping = {letter : str(index + 1) for index, letter in enumerate(string.ascii_lowercase)}
        conversion = [mapping[c] for c in s]
        num = ''.join(conversion)

        while k > 0:
            number = 0
            for c in num:
                number += int(c)
            num = str(number)
            k -= 1
        return int(num)