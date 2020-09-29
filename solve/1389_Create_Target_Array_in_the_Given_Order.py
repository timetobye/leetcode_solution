class Solution:
    def createTargetArray(self, nums, index):
        target = []

        for pair in zip(nums, index):
            target.insert(pair[1], pair[0])

        return target



if __name__ == "__main__":
    solution = Solution()
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]
    result = solution.createTargetArray(nums, index)
    print(result)