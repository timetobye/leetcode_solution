class Solution:
    def numJewelsInStones(self, J, S):
        J_components = list(J)
        S_components = list(S)

        counter = 0

        for J_component in J_components:
            component_count = S_components.count(J_component)

            counter += component_count

        return counter


from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels, stones):
        counter_stones = Counter(stones)
        count = 0

        for jewel in jewels:
            if jewel in counter_stones:
                count += counter_stones[jewel]

        return count



