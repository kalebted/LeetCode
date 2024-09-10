class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0
        for _ in range(32):
            reversed_n = (reversed_n << 1) | (n & 1)
            n >>= 1
        return reversed_n

        # bin_str = str(n)
        # rev_bin = ""
        # for i in reversed(bin_str):
        #     rev_bin += bin_str[i]
        # print(rev_bin)

        # # Convert the integer to its binary representation (removing '0b' prefix)
        # bin_str = bin(n)[2:]
        
        # # Reverse the binary string
        # rev_bin = bin_str[::-1]
        
        # # Convert the reversed binary string back to an integer
        # reversed_num = int(rev_bin, 2)
        
        # return reversed_num