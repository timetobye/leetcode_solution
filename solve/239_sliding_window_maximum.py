from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        q = deque()
        result = []
        for index, value in enumerate(nums):
            while q and q[-1][1] < value:
                # 부분적으로 뒤의 값보다 작기 때문에 어차피 필요가 없음
                q.pop()
            # nums 에서 가져온 값의 index, value를 저장한다.
            q.append([index, value])
            if index >= (k-1):
                # 큰 값이 계속 좌측에 남아 있을 수 있으며, 윈도우 size 밖의 값으로 존재 할 수 있다.
                # nums = [1, 3, 1, 2, 0, 5], k = 3

                # 가장 큰 값을 걸러내야 하는데, value 비교로 걸러낼 경우 에러가 생김 nums = [1]; k=1
                # 그래서 index 값으로 비교해서 index 가 같으면 가장 왼쪽 값을 제거(범위 밖의 수 이므로)
                if q[0][0] == index - k:
                    q.popleft()

                result.append(q[0][1])

        return result


if __name__ == "__main__":
    solution = Solution()
    # nums = [1, 3, -1, -3, 5, 3, 6, 7]; k = 3
    # nums = [1,3,1,2,0,5]; k = 3
    nums = [1]; k=1
    res = solution.maxSlidingWindow(nums, k)
    print(res)