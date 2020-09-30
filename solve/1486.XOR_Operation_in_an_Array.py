from functools import reduce


class Solution:
    def xorOperation(self, n, start):
        nums = [start + 2*i for i in range(n)]

        result = reduce(lambda a, b: a ^ b, nums, 0)

        return result


if __name__ == "__main__":
    solution = Solution()
    res = solution.xorOperation(5, 0)
    print(res)
