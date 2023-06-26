class Solution:
    def longestPalindrome(self, s):
        def expand(left, right):
            # 특정 지점에서 아래 조건에 맞을 경우(팰린드롬), 확장하는 방식으로 결과를 추림
            # <->, <--->, <----->, ....
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1 : right]

        # 예외 처리
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(0, len(s) - 1):
            # 두 개의 포인터가 0 부터 마지막까지 훓고 지나감
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

        return result


if __name__ == "__main__":
    solution = Solution()
    s = "babad";
    s = "aacabdkacaa"
    res = solution.longestPalindrome(s)
    print(res)



"""
from pprint import pprint
from collections import Counter

class Solution:
    def longestPalindrome(self, s):
        rev_s = s[::-1]
        n, m = len(s), len(rev_s)

        dp = [[None for i in range(n + 1)] for j in range(m + 1)]

        max_position = 0
        position_y, position_x = 0, 0

        for j in range(m + 1):
            for i in range(n + 1):
                if i == 0 or j == 0:
                    dp[j][i] = 0

        for j in range(1, m + 1):
            for i in range(1, n + 1):
                if rev_s[j - 1] == s[i - 1]:
                    dp[j][i] = dp[j - 1][i - 1] + 1
                    if dp[j][i] > max_position:
                        max_position = dp[j][i]
                        position_y, position_x = j, i
                else:
                    dp[j][i] = 0

        def chase_dp(m, n):
            chase_string_list = []
            while dp[m][n] != 0:
                if dp[m][n] == dp[m - 1][n]:
                    m -= 1
                elif dp[m][n] == dp[m][n - 1]:
                    n -= 1
                else:
                    chase_string_list.append(s[n - 1])
                    m -= 1
                    n -= 1

            reversed_chase_string_list = reversed(chase_string_list)
            chase_string = "".join(reversed_chase_string_list)

            return chase_string

        # pprint(dp)
        return chase_dp(position_y, position_x)


if __name__ == "__main__":
    solution = Solution()
    s = "babad";
    s = "aacabdkacaa"
    res = solution.longestPalindrome(s)
    print(res)
"""
