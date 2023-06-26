class Solution:
    def reorderLogFiles(self, logs):
        digits, letters = [], []

        for log in logs:
            # isdigit 은 문자열이 숫자로만 이루어져 있는지, 문자가 포함되어 있는지 판별
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # 정렬을 lambda 연산을 이용하여 처리
        # 정렬 첫 번째, 두 번째 순서로 명명
        letters.sort(key=lambda x : (x.split()[1:], x.split()[0]))

        return letters + digits


if __name__ == "__main__":
    solution = Solution()
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    res = solution.reorderLogFiles(logs)
    print(res)


"""
def func(x):
    return x.split()[1:], x.split()[0]

s.sort(key=func)
"""