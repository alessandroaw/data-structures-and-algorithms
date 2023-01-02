# array and hashing
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Idea:
        # Anagram will have same character count in each string
        if len(s) != len(t):
            return False

        # Create dictionary to count the number of character on string s
        d = dict()
        for c in s:
            d[c] = d.get(c, 0) + 1

        # Substract one for each found character on string t
        # If the count reach -1 (meaning character is not in s) than its false
        for c in t:
            d[c] = d.get(c, 0) - 1
            if d[c] < 0:
                return False

        return True
