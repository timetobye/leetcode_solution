class Solution:
    def numIdenticalPairs(self, nums):
        count = 0
        length = len(nums)

        for i in range(length):
            for j in range(i, length):
                if (nums[i] == nums[j]) and (i < j):
                    count += 1

        return count


if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,1,1,3]

    result = solution.numIdenticalPairs(nums)

    print(result)
