class Solution:
    def find(self, x, parent, equation):
        if x != parent[x]:
            par, equ = self.find(parent[x], parent, equation)
            parent[x] = par
            equation[x] *= equ
        return parent[x], equation[x]
    def union(self, x, y, val,  parent, equation, size):
        parent_a, equ_a = self.find(x, parent, equation)
        parent_b, equ_b = self.find(y, parent, equation)
        equ = val * equ_b/equ_a
        if parent_a != parent_b:
            if size[parent_a] >= size[parent_b]:
                parent_b, parent_a, equ = (parent_a, parent_b, 1/equ)

            parent[parent_a] = parent_b
            size[parent_b] += size[parent_a]
            equation[parent_a] = equ

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        parent = defaultdict(str)
        size = defaultdict(int)
        equation = defaultdict(lambda: 1.0)

        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            if a not in parent:
                parent[a] = a
            if b not in parent:
                parent[b] = b
             
            self.union(a, b, val, parent, equation, size)
        ans = []
        for a, b in queries:
            if a not in parent or b not in parent:
                ans.append(-1)
            else:
                parent_a, ans_a = self.find(a, parent, equation)
                parent_b, ans_b = self.find(b, parent, equation)
                if parent_a != parent_b:
                    ans.append(-1)
                else:
                    ans.append(ans_a/ans_b)

        return ans
        
        