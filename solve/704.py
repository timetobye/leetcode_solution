class Solution:
    def search(self, nums, target):
        length = len(nums)
        left, right = 0, length - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1

            elif nums[mid] == target:
                return mid

        return -1

from bisect import bisect_left

class Solution:
    def search(self, nums, target):
        index = bisect_left(nums, target)

        if (index < len(nums)) and (nums[index] == target):
            return index

        else:
            return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    solution = Solution()
    res = solution.search(nums, target)
    print(res)