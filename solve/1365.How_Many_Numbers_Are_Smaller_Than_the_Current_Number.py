class Solution:
    def smallerNumbersThanCurrent(self, nums):
        length = len(nums)
        result = [0 for _ in range(length)]

        for idx, num in enumerate(nums):
            count = [1 for value in nums if value < num]
            sum_count = sum(count)
            result[idx] += sum_count

        return result