class Solution:
    def numberOfSteps(self, num):
        count = 0

        while num > 0:
            if (num % 2) == 0:
                num = num // 2
                count +=1
            else:
                num -= 1
                count += 1

        return count


if __name__ == "__main__":
    num = 14

    solution = Solution()
    res = solution.numberOfSteps(num)
    print(res)