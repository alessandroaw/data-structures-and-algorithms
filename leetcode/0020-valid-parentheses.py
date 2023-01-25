class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        d = {")": "(", "}": "{", "]": "["}

        stack = []

        for c in s:
            if not stack or (not c in d):
                stack.append(c)
            else:
                last = stack.pop()
                if last != d[c]:
                    return False

        return not stack
