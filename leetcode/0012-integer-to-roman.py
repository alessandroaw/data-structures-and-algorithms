class Solution:
    def intToRoman(self, num: int) -> str:
        # get the number form the back
        res = ''
        digit = 0
        ones = ['I', 'X', 'C', 'M']
        fives = ['V', 'L', 'D']
        while num != 0:
            # get the last digit (remainder)
            r = num % 10

            # get the symbol for one in this digit
            one = ones[digit]
            if r == 9:
                # get the symbol for ten in this digit
                ten = ones[digit + 1]
                # nine is ten with one prefix
                res = one + ten + res
            elif r < 4:
                # below four is repeating the one character
                res = one * r + res
            else:
                # get the symbol for five in this digit
                five = fives[digit]
                # 4 - 8 is using the combination of prefix and suffix
                # 4 is is only using prefix
                # 5 is not using prefix and suffix
                # 7-8 is only using suffix
                # the prefix and suffix condition can be writen as this:
                prefix = (1 if r == 4 else 0) * one
                suffix = max(0, r - 5) * one
                res = prefix + five + suffix + res

            # don't forget to move the iterator
            num = num // 10
            digit += 1
        return res
