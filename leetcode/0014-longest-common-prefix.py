class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # handling edge case, when there is only one string
        # the string itself is the common prefix
        if len(strs) == 1:
            return strs[0]

        last_common = 0
        # iterate for each character in the first string
        for i in range(len(strs[0])):
            last_common = i
            curr_c = strs[0][i]

            # iterate each string on a given character position
            for s in strs:
                # if string is shorter than other string
                # or string have difference character
                if i >= len(s) or s[i] != curr_c:
                    return s[:last_common]

        # if all passed than return the whole first string
        return strs[0]
