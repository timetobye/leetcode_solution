class Solution:
    def decompressRLElist(self, nums):
        devided_length = len(nums) // 2
        result = []

        for i in range(devided_length):
            freq, val = [nums[2*i], nums[2*i+1]]

            for j in range(freq):
                result.append(val)

        return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    solution = Solution()
    res = solution.decompressRLElist(nums)
    print(res)