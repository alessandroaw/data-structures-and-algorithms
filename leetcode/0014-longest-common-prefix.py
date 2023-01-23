class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        last_common = 0
        for i in range(len(strs[0])):
            last_common = i
            curr_c = strs[0][i]

            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[j][i] != curr_c:
                    return strs[0][:last_common]

        return strs[0][:last_common + 1]
