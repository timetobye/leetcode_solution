class Solution:
    def shuffle(self, nums, n):
        result = []

        for i in range(n):
            result += [nums[i], nums[i + n]]

        return result


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 5, 1, 3, 4, 7]
    n = 3

    result = solution.shuffle(nums, n)

    print(result)
