class Solution:
    def kidsWithCandies(self, candies_list, extra_candies):
        max_number = max(candies_list)
        result = [True for _ in range(len(candies_list))]

        for idx, candy in enumerate(candies_list):
            if candy == max_number:
                continue

            if (candy + extra_candies) >= max_number:
                continue
            else:
                result[idx] = False

        return result


if __name__ == "__main__":
    candies_list = [2, 3, 5, 1, 3]
    extraCandies = 3

    solution = Solution()
    res = solution.kidsWithCandies(candies_list, extraCandies)
    print(res)



