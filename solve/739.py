class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        daily = [0 for _ in range(len(temperatures))]

        for idx, temperature in enumerate(temperatures):
            while stack and stack[-1][-1] < temperature:
                temp_idx, temp_temp = stack.pop()
                daily[temp_idx] = idx - temp_idx

            stack.append([idx, temperature])

        return daily


class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        daily = [0 for _ in range(len(temperatures))]

        for idx, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                last_index = stack.pop()
                daily[last_index] = idx - last_index

            stack.append(idx)

        return daily


if __name__ == "__main__":
    solution = Solution()
    temperatures = [73,74,75,71,69,72,76,73];
    temperatures = [30,60,90]
    result = solution.dailyTemperatures(temperatures)

    print(result)