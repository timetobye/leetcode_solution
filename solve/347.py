from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count_numbs = Counter(nums)
        result = count_numbs.most_common(k)

        return list(zip(*result))[0]


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2

    solution = Solution()
    res = solution.topKFrequent(nums, k)
    print(res)