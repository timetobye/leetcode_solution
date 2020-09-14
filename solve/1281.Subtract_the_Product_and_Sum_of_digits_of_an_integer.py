from operator import mul
from functools import reduce


class Solution:
    def subtractProductAndSum(self, n):
        nums = [int(value) for value in list(str(n))]

        product_of_digits = reduce(mul, nums, 1)  # 마지막 1은 최종 결과에 1배, 2이면 2배, 3이면 3배
        sum_of_digits = sum(nums)
        result = product_of_digits - sum_of_digits

        return result


if __name__ == "__main__":
    num = 12345

    solution = Solution()
    res = solution.subtractProductAndSum(num)
    print(res)