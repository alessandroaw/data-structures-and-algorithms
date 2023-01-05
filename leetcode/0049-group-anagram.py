# array and hashing
# TC: O(n m log m)
# SC: O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g = dict()
        # iterate through list
        for s in strs:
            # check if current is anagram of known group (need some key)
            # if true add to list
            # else create a new group
            sorted_s = "".join(sorted(s))
            g[sorted_s] = g.get(sorted_s, []) + [s]

        # return the list of group
        return g.values()
