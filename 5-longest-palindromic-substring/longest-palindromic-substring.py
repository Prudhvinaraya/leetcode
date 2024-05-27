class Solution:
    def longestPalindrome(self, s: str) -> str:
        modified_s = "#"
        for char in s:
            modified_s += char + "#"

        n = len(modified_s)
        P = [0] * n  # Array to store the length of palindromes at each position
        C, R = 0, 0  # Center and right boundary of the current palindrome

        max_len = 0  # Maximum length of a palindrome found
        max_center = 0  # Center of the palindrome with maximum length

        for i in range(n):
            if i < R:
                mirror = 2 * C - i  # Mirror position of i
                P[i] = min(R - i, P[mirror])

            # Expand around the current character
            a, b = i + (1 + P[i]), i - (1 + P[i])
            while a < n and b >= 0 and modified_s[a] == modified_s[b]:
                P[i] += 1
                a += 1
                b -= 1

            # Update the center and right boundary if needed
            if i + P[i] > R:
                C, R = i, i + P[i]

            # Update the maximum length and its center
            if P[i] > max_len:
                max_len = P[i]
                max_center = i

        start = (max_center - max_len) // 2  # Start index of the longest palindrome
        end = start + max_len  # End index of the longest palindrome

        return s[start:end]