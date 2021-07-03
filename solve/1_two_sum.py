"""
조합으로 풀면 마지막 케이스에서 걸린다.

결국 빠르게 탐색할 수 있는 방법으로 생각을 전환하였다.
"""


class Solution:
    def twoSum(self, numbers, target_number):
        for x_index, number in enumerate(numbers):
            # x + y = target_number
            y = target_number - number

            try:
                y_index = numbers[x_index + 1:].index(y) + 1 + x_index

                return [x_index, y_index]

            except:
                continue


if __name__ == "__main__":
    solution = Solution()
    Given_nums = [3, 2, 4]
    target = 6

    result = solution.twoSum(Given_nums, target)

    print(result)

# 위의 코드를 수정
# O(n^2) 이 나오기는 하지만 in 연산 쪽이 훨씬 더 가볍고 빠름
class Solution:
    def twoSum(self, numbers, target_number):
        for x_index, number in enumerate(numbers):
            y = target_number - number

            if y in numbers[x_index + 1:]:
                return [x_index, numbers[x_index + 1:].index(y) + 1 + x_index]



class Solution:
    """
    중복 되는 값이 있더라도, 앞에서 인덱스가 처리되기 때문에 문제 없음
    """
    def twoSum(self, numbers, target_number):
        nums_dict = {}
        for x_index, number in enumerate(numbers):
            nums_dict[number] = x_index

        # print(nums_dict)
        for x_index, number in enumerate(numbers):
            value = target_number - number

            # if value in nums_dict and x_index != nums_dict[value]:
            #     return [x_index, nums_dict[value]]

            if nums_dict.get(value) and x_index != nums_dict[value]:
                return [x_index, nums_dict[value]]

    def twoSum_restructure(self, numbers, target_number):
        nums_dict = {}
        for x_index, number in enumerate(numbers):
            value = target_number - number

            # if value in nums_dict and x_index != nums_dict[value]:
            #     return [x_index, nums_dict[value]]

            if value in nums_dict:
                return [nums_dict[value], x_index]
            nums_dict[number] = x_index


if __name__ == "__main__":
    solution = Solution()
    Given_nums = [3, 3]
    target = 6

    result = solution.twoSum_restructure(Given_nums, target)

    print(result)


"""legacy code
time limit

from itertools import combinations


class Solution:
    def twoSum(self, numbers, target_number):
        idx_of_numbers = [int(x) for x in range(len(numbers))]

        for combination in combinations(idx_of_numbers, 2):
            combination_sum = numbers[combination[0]] + numbers[combination[1]]

            if combination_sum == target_number:
                return [combination[0], combination[1]]

"""