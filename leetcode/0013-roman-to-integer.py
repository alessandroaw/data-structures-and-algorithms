number_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = 0
        length = len(s)
        for i in range(length):
            roman_value = number_dict[s[i]]
            if i < length - 1 and number_dict[s[i+1]] > roman_value:
                value = value - roman_value
            else:
                value = value + roman_value

        return value
