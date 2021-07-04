class Solution:
    def productExceptSelf(self, nums):




if __name__ == "__main__":
    solution = Solution()
    nums = [-1,1,0,-3,3]
    result = solution.productExceptSelf(nums)

    print(result)


"""
from collections import deque
from functools import reduce

class Solution:
    def productExceptSelf(self, nums):
        q = deque(nums)
        results = []

        for i in range(len(q)):
            q.rotate(-1)
            result = reduce(lambda x, y: x * y, list(q)[0:-1])
            results.append(result)

        return results
"""