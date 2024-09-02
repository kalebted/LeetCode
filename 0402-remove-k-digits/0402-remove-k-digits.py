class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k > 0 and stack and stack[-1] > c:
                k -= 1
                stack.pop()
            stack.append(c)

        # Adjust the stack in case k is still greater than 0
        stack = stack[:len(stack) - k]

        # Convert stack back to string and remove leading zeros
        res = "".join(stack).lstrip('0')
        
        # Return '0' if the resulting string is empty
        return res if res else "0"