def g(grades):
    ans = []
    for i in range(len(grades)):
        dif = 5 - grades[i] % 5
        if grades[i] < 38:
            ans.append(grades[i])
        
        elif dif < 3:
            ans.append(grades[i] + dif)
        else:
            ans.append(grades[i])

    return ans