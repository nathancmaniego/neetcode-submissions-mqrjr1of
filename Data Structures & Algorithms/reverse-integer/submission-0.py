class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647
        
        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            # checks if greather than 214748364 
            # or if equal and digit is greater than 7
            if (res > MAX // 10 or
                res == MAX // 10 and digit >= MAX % 10):
                return 0
            # checks if less than 214748364
            # or if equal and digit is less than 8 i.e overflow
            if (res < MIN // 10 or
                res == MIN // 10 and digit <= MIN % 10):
                return 0
            res = (res * 10) + digit
        return res