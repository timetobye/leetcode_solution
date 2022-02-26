"""
prefix sum 를 바탕으로 접근
원소 [a, b, c, d] 를 가진다고 할 때
- 최종 결과를 예측해보면 [dcb, dca, dba, cba] 이다. 이것을 분할 해서 나타낸 후 그 결과를 다시 곱할 것이다.
- 좌측에서 우측으로 순차적으로 곱하면 [1, a, ab. abc] 가 된다.
- 우측에서 좌측으로 순차적으로 곱하면 [dcb, dc, d, 1] 가 된다.
- index 에 해당하는 경우를 각각 곱하면 답이 나온다.
참고 : https://m.blog.naver.com/withham1/221320996067

O(n) 으로 풀어야 하기 때문에 아래 주석 처리한 코드로는 풀 수 없다.
"""


class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        left_to_right = [1 for i in range(length)]
        right_to_left = [1 for i in range(length)]
        answer = [1 for i in range(length)]

        for i in range(1, length):
            left_to_right[i] = left_to_right[i - 1] * nums[i - 1]
            right_to_left[i] = right_to_left[i - 1] * nums[length - i]

        for i in range(length):
            answer[i] = left_to_right[i] * right_to_left[length - i - 1]

        return answer


if __name__ == "__main__":
    solution = Solution()
    # nums = [-1, 1, 0, -3, 3]
    nums = [1, 2, 3, 4]
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

"""
from functools import reduce

class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        product_list = []

        for i in range(length):
            nums[0], nums[i] = nums[i], nums[0]
            res = reduce(lambda x, y: x * y, nums[1:])
            product_list.append(res)

        return product_list
"""