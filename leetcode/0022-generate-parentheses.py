class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combos = []

        def genPar(open, close, combo):
            if close == n:
                combos.append(combo)

            if open > close:
                genPar(open, close + 1, combo + ")")

            if open < n:
                genPar(open + 1, close, combo + "(")

        genPar(1, 0, "(")

        return combos
