class Solution:
    def mySqrt(self, x):
        digit = 1
        while True:
            if (digit * digit) > x:
                break
            digit += 1

        return digit - 1

import math

class Solution:
    def mySqrt(self, x):
        return int(math.sqrt(x))
