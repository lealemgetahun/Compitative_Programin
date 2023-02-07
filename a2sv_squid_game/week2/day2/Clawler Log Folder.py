class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for log in logs:
            if stack and log == "../":
                stack.pop()
            else:
                if log == "./" or log == "../":
                    continue
                stack.append(log)
        return len(stack)