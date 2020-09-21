class Solution:
    def trailingZeroes(self, n: int) -> int:
        number = 5
        count = 0

        while n >= number:
            count += n // number
            number = number * 5

        return count