"""
https://docs.python.org/3/library/collections.html#collections.defaultdict
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)

        for word in strs:
            # ' '.join(sorted(word)) key 가 됨
            # 그리고 word 추가
            anagrams[' '.join(sorted(word))].append(word)
            # print(anagrams)

        return list(anagrams.values())


if __name__ == "__main__":
    solution = Solution()
    strings = ["eat","tea","tan","ate","nat","bat"]
    res = solution.groupAnagrams(strings)
    print(res)