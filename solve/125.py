import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = " ".join(re.findall(r'[a-zA-Z0-9]', s))
        strings = result.lower()
        reversed_strings = strings[::-1]

        if strings == reversed_strings:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    strings = "0P"
    res = solution.isPalindrome(strings)
    print(res)

"""
참고 문서
- https://it-neicebee.tistory.com/43
  - isalnum()
"""


"""
legacy code

class Solution:
    def isPalindrome(self, s: str) -> bool:
        find_result = re.findall(r'\w', s)
        result = [x.lower() for x in find_result if x != "_"]

        length = len(result)

        for i in range(length//2):
            if result[i] != result[(i+1) * -1]:
                return False
        else:
            return True
"""