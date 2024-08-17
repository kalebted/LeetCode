class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 2^31 = 2147483648 - 1
        dd = abs(dividend)
        ds = abs(divisor)
        output = 0

        while dd >= ds:
            tmp = ds
            mul = 1
            while dd >= tmp:
                dd -= tmp
                output += mul
                mul += mul
                tmp += tmp

        if(dividend < 0 and divisor > 0) or (divisor < 0 and dividend >= 0):
            output = -output

        return min(2147483647, max(-2147483648, output))