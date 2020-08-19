class Solution:
    def runningSum(self, nums):
        cum_numbers = []

        value = 0
        for idx, _ in enumerate(nums):
            value += nums[idx]
            cum_numbers.append(value)

        return cum_numbers


# class Solution:
#     def runningSum(self, nums):
#         length = len(nums)
#         dp = [0 for _ in range(length)]
#         dp[0] = nums[0]
#
#         for i in range(length-1):
#             dp[i+1] = dp[i] + nums[i+1]
#
#         return dp


if __name__ == "__main__":
    solution = Solution()
    Given_nums = [3,1,2,10,1]

    result = solution.runningSum(Given_nums)

    print(result)
