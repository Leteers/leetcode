import math
class Solution:
    def pivotInteger(self, n: int) -> int:
        x = math.sqrt(n * (n + 1) / 2)

        if x % 1 != 0:
            return -1
        else:
            return int(x)