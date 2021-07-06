class Solution:
    def fib(self, n):
        if n <= 1:
            return n

        dp = [None for _ in range(n + 1)]
        dp[0], dp[1] = 0, 1

        def calc_dp(n):
            if dp[n] is None:
                dp[n] = calc_dp(n - 2) + calc_dp(n - 1)

            return dp[n]

        return calc_dp(n)


class Solution:
    def fib(self, n):
        if n <= 1:
            return n

        dp = [None for _ in range(n + 1)]
        dp[0], dp[1] = 0, 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[n]


class Solution:
    def fib(self, n):
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x + y

        return x

if __name__ == "__main__":
    solution = Solution()
    n = 10
    result = solution.fib(n)

    print(result)