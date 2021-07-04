"""
정말 어렵다.
책을 보고 겨우 풀을 정도였음
스택으로 처리하는 방법은 이해를 하지 못함
"""

class Solution:
    def trap(self, height):
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        # print(f'init max : left_max : {left_max}, right_max : {right_max}')

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            # print(f'max : left_max : {left_max}, right_max : {right_max}')

            if left_max <= right_max:
                # print(f'left')
                # print(left_max, height[left])
                volume += left_max - height[left]
                # print(volume)
                left += 1
            else:
                # print(f'right')
                volume += right_max - height[right]
                # print(volume)
                right -= 1

        return volume


if __name__ == "__main__":
    solution = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = solution.trap(height)

    print(result)

from pprint import pprint

class Solution:
    def trap(self, height):
        # stack 은 기준벽이라고 생각하면 쉽다. 이전 높이를 저장해둠
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점 만남
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                print(top, len(stack))
                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
            pprint(stack)

        return volume


if __name__ == "__main__":
    solution = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = solution.trap(height)

    print(result)