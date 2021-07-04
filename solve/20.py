class Solution:
    def isValid(self, s):
        stack = []
        strings_dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char not in strings_dict:
                stack.append(char)
            # stack 에 넣은 char에 대응하는 값이 없을 경우 잘못 들어간 경우이다.
            elif not stack or strings_dict[char] != stack.pop():
                return False

        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    s = "()[]{}"
    result = solution.isValid(s)

    print(result)