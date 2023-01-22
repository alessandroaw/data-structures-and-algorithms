class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        d = dict()
        length = 0
        max_length = 0
        for i, c in enumerate(s):
            d[c] = d.get(c, 0) + 1
            length += 1

            while d[c] > 1:
                d[s[l]] -= 1
                length -= 1
                l += 1

            max_length = max(max_length, length)

        return max_length
