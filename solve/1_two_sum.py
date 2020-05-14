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