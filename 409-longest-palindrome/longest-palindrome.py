class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = {}
        for c in s:
            if c in hm:
                hm[c] += 1
            else:
                hm[c] = 1

        ans = 0
        isFirstOdd = False

        for key in hm:
            if hm[key] % 2 == 0:
                ans += hm[key]
            else:
                ans += hm[key]
                if not isFirstOdd:
                    isFirstOdd = True
                else:
                    ans -= 1

        return ans