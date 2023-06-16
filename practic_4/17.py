https://www.codewars.com/kata/57fae964d80daa229d000126/train/python

def remove(s):
    if s.endswith('!'):
        return s[:-1]
    else:
        return s