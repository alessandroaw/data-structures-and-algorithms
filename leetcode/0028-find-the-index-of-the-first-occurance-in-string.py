class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l, r = -1, 0
        next_l = -1
        count = 0
        len_needle = len(needle)
        len_haystack = len(haystack)

        while r < len_haystack:
            c = haystack[r]

            if next_l <= l and c == needle[0]:
                next_l = r

            if c == needle[count]:
                count += 1

                if count == 1:
                    l = r

                if count == len_needle:
                    return l
                r += 1

            else:
                if next_l > l:
                    l = next_l
                    r = l
                    count = 1
                else:
                    count = 0
                r += 1

        return -1
