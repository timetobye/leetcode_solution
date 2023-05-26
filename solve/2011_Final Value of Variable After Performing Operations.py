class Solution:
    def finalValueAfterOperations(self, operations):
        ans = operations.count("++X") + operations.count("X++") - operations.count("--X") - operations.count("X--")

        return ans