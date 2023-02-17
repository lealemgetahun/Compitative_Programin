class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def back(op, cl, path):
            if op == n and cl == n:
                ans.append("".join(path))
                return
            if op < n:
                path.append("(")
                back(op + 1, cl, path)
                path.pop()
            if cl < op:
                path.append(")")
                back(op , cl + 1, path)
                path.pop()
        back(0,0,[])
        return ans