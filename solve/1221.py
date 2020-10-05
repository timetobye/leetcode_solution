class Solution:
    def balancedStringSplit(self, s):
        strings = list(s)

        count = 0
        result = 0

        for string in strings:
            if string == 'R':
                result +=1
            else:
                result -=1

            if result == 0:
                count +=1

        return count