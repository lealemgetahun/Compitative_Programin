class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letter_logs = []
        digit_logs = []
        for log in logs:
            log_ls = log.split()
            identifier = log_ls[0]
            temp = [" ".join(log_ls[1:]), identifier]
            if log_ls[1].isnumeric():
                digit_logs.append(log)
            else:
                letter_logs.append(temp)
        letter_logs.sort()
        ans = []
        for log in letter_logs:
            temp = log[1] + " " + log[0]
            ans.append(temp)
        ans.extend(digit_logs)
        return ans