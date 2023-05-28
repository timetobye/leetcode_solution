class Solution:
    def restoreString(self, s, indices):
        ziped_components = zip(s, indices)
        sorted_result = sorted(ziped_components, key=lambda x : x[1])

        chr_values = [chr_value[0] for chr_value in sorted_result]
        result = ''.join(chr_values)

        return result


if __name__ == "__main__":
    s = "abc"
    indices = [0,1,2]

    solution = Solution()
    res = solution.restoreString(s, indices)
    print(res)