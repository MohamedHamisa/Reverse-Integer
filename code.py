class Solution:
    def reverse(self, x: int) -> int:
        neg =  False
        if x < 0:
            neg = True
            x = -x
        value = int(str(x)[::-1])
        if value<2**31-1 or (value == 2**31 and neg):
            if neg:
                return - value
            else:
                return  value
        else:
            return 0
