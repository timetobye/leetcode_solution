class Solution:
    def isPalindrome(self, number):
        string_number = str(number)
        reversed_string_number = string_number[::-1]

        if string_number == reversed_string_number:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    result = sol.isPalindrome(-121)
    print(result)