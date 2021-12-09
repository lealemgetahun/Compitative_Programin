def fizzBuzz(self, n: int) -> List[str]:
        ans = [0]*n
        for i in range (0,n):
            index = i + 1
            if index % 3 == 0 and index % 5 == 0:
                ans[i] = "FizzBuzz"
            elif index % 3 == 0:
                ans[i] = "Fizz"
            elif index % 5 == 0:
                ans[i] = "Buzz"
            else:
                ans[i] = str(index)
        return ans