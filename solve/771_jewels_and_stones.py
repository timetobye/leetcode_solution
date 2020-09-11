class Solution:
    def numJewelsInStones(self, J, S):
        J_components = list(J)
        S_components = list(S)

        counter = 0

        for J_component in J_components:
            component_count = S_components.count(J_component)

            counter += component_count

        return counter


if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"

    solution = Solution()
    res = solution.numJewelsInStones(J, S)
    print(res)
