class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {}
        def calc(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            if n == -1:
                return 1/x

            if n in memo:
                return memo[n]
            
            memo[n] = self.myPow(x, n // 2) ** 2
            if n % 2 == 1:
                memo[n] *= x

            return memo[n]
        return calc(x, n)