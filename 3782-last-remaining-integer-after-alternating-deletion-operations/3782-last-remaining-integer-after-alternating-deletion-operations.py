class Solution(object):
    def lastInteger(self, n):
        result = 1
        step = 1
        left = True

        while n > 1:

            if not left and n % 2 == 0:
                result += step

            n = (n + 1) // 2
            step *= 2
            left = not left

        return result
        