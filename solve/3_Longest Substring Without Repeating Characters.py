class Solution:
    def lengthOfLongestSubstring(self, s):
        start = 0
        used = {}
        max_length = 0

        for idx, char in enumerate(s):

            # 그런데 앞에 있는 항목이 뒤에서 사용되면서 최장 길이를 가지게 할 수도 있다.
            # 슬라이딩 윈도우의 바깥에 있는 문자는 예전에 등장한 적이 있더라도 지금은 무시해야 함. 조건 추가
            if char in used and start <= used[char]:
                # used[char] 를 하면 해당 문자의 위치를 반환하며, 현재 위치를 지정한다.
                # 한 칸씩 이동하니까 시작점도 1칸 이동
                start = used[char] + 1
            else:
                max_length = max(max_length, idx - start + 1)

            # 조회한 문자의 idx 번호를 넣기
            used[char] = idx
            print(f'char : {char}, start : {start}, idx : {idx}, used : {used}')
        return max_length


if __name__ == "__main__":
    solution = Solution()
    s = "abcabcbb"
    res = solution.lengthOfLongestSubstring(s)
    print(res)