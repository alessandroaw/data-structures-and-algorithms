class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        isWord = False
        start = 0
        end = len(s)
        for i in range(len(s)-1, -1, -1):
            if isWord and s[i] == " ":
                break

            if s[i].isalnum():
                if not isWord:
                    isWord = True
                    end = i + 1
                start = i

        return end - start
