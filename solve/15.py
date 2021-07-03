class Solution:
    def threeSum(self, nums):
        len_nums = len(nums)
        # 정렬을 하는 이유 중 하나는 포인터를 움직일 때 정렬이 되어 있으면 합계를 기준으로 옮기는 방향을 알 수 있음
        nums.sort()
        results = []

        for i in range(len_nums - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len_nums - 1

            while left < right:
                point_sum = nums[i] + nums[left] + nums[right]

                if point_sum < 0:
                    # 정렬이 되어 있기 때문에 더 큰 값을 찾기 위해 왼쪽에서 오른쪽으로 이동
                    left += 1
                elif point_sum > 0:
                    # 정렬이 되어 있기 때문에 더 작은 값을 찾기 위해 오른쪽에서 왼쪽으로 이동
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        # 중복이 있을 경우 건너 뛰기
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results

if __name__ == "__main__":
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    result = solution.threeSum(nums)

    print(result)


"""
O(n^3) 으로 타임 아웃
class Solution:
    def threeSum(self, nums):
        len_nums = len(nums)
        nums.sort()
        results = []

        for i in range(len_nums - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len_nums - 1):
                # 중복 체크
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                for k in range(j + 1, len_nums):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue

                    if (nums[i] + nums[j] + nums[k]) == 0:
                        results.append([nums[i], nums[j], nums[k]])

        return results

"""




"""
from itertools import combinations


class Solution:
    def threeSum(self, nums):
        result = []

        for numbers in combinations(nums, 3):
            if sum(numbers) == 0:
                sort_number = sorted(list(numbers))
                if sort_number not in result:
                    result.append(sort_number)

        return result
"""