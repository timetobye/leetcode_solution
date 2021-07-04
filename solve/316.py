from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s):
        stack = []
        strings_counter = Counter(s)

        for char in s:
            # 사용하는 문자 카운트 감소
            strings_counter[char] -= 1

            if char in stack:
                # 존재하면 쌓지 않아도 된다.
                continue

            # counter 숫자가 0이 아니라는 것은 뒤에 문자가 존재한다는 것을 의미
            # 'a' < 'b' : True 이다...문자열도 비교가 가능하다. 사전 순서대로

            while stack and char < stack[-1] and strings_counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)

        return ''.join(stack)


if __name__ == "__main__":
    solution = Solution()
    s = "bcabc"
    result = solution.removeDuplicateLetters(s)

    print(result)