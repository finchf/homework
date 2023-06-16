https://www.codewars.com/kata/5a805d8cafa10f8b930005ba/train/python


import math

def nearest_sq(n):
    m = math.sqrt(n)
    if m == int(m):
        return n
    else:
        min_sqr = int(m) ** 2
        max_sqr = int(m+1) ** 2
        if n - min_sqr < max_sqr -n:
            return min_sqr
        else:
            return max_sqr