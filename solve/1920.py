class Solution:
    def buildArray(self, nums):
        ans = [nums[i] for i in nums]

        return ans


if __name__ == "__main__":
    solution = Solution()
    Given_nums = [3, 2, 4]
    result = solution.buildArray(Given_nums)
