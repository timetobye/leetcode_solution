class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 왼쪽에서 시작하는 번호, 오른쪽에서 시작하는 번호
        left, right = 0, len(s) - 1

        # 오른쪽이 작아지면 종료
        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1
