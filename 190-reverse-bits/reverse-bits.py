class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_bits = 0
        for _ in range(32):  # Assuming we are dealing with a 32-bit integer
            reversed_bits = (reversed_bits << 1) | (n & 1)
            n >>= 1
        return reversed_bits

        