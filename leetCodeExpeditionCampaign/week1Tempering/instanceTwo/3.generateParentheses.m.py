class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []


        def backtracking(opening, closing, curr):
            if opening + closing == n * 2:
                res.append("".join(curr))
                return

            if opening < n:
                curr.append("(")
                backtracking(opening + 1, closing, curr)
                curr.pop()
            
            if closing < opening:
                curr.append(")")
                backtracking(opening, closing + 1, curr)
                curr.pop()

        backtracking(0, 0, [])
        return res



        

