class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        checks = []
        openTags = ['(', '{', '[']
        closeTags = [')', '}', ']']
        closeTagsPair = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        if len(s) == 1:
            return False

        for c in s:
            if c in openTags:
                checks.append(c)
            else:
                try:
                    if c in closeTags and closeTagsPair[c] == checks[-1]:
                        checks.pop()
                    else:
                        return False
                except:
                    return False

        return not bool(checks)
