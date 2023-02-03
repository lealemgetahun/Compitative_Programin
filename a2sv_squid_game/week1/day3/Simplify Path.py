class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        
        for i in range(len(path)):
            if stack and path[i] == "..":
                stack.pop()
            else:
                if path[i] != "" and path[i] != "." and path[i] != "..":
                    stack.append(path[i])
        # print(stack)
        ans = "/"
        return ans + "/".join(stack)
