class Solution:
    def maximumWealth(self, accounts):
        maximum_value = 0

        for account in accounts:
            sum_account = sum(account)

            if sum_account > maximum_value:
                maximum_value = sum_account

        return maximum_value


if __name__ == "__main__":
    solution = Solution()
    arr = [[1,2,3],[3,2,1]]
    res = solution.maximumWealth(arr)
    print(res)
