class Solution:
    def defangIPaddr(self, address):
        result = address.replace(".", "[.]")

        return result


if __name__ == "__main__":
    address = "1.1.1.1"

    solution = Solution()
    res = solution.defangIPaddr(address)
    print(res)



