class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        sum_result = 0

        for i in range(0, len(nums), 2):
            sum_result += nums[i]

        return sum_result

class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[::2])


if __name__ == "__main__":
    solution = Solution()
    nums = [1,4,3,2]
    result = solution.arrayPairSum(nums)

    print(result)