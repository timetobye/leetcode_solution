class Solution:
    def maxSubArray(self, nums):
        length = len(nums)
        dp = [None for _ in range(length)]
        dp[0] = nums[0]

        def calc_dp(n):
            if dp[n] is None:
                dp[n] = nums[n] + max(calc_dp(n - 1), 0)

            return dp[n]

        calc_dp(length - 1)

        return max(dp)


class Solution:
    def maxSubArray(self, nums):
        length = len(nums)
        dp = [None for _ in range(length + 1)]
        dp[0] = nums[0]

        for i in range(1, length):
            dp[i] = nums[i] + max(dp[i - 1], 0)

        return max(dp)