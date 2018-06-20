from collections import Counter

def scramble(s1, s2):
    frequencies = list(map(Counter, [s1, s2]))
    for char in s2:
        if char not in frequencies[0] or frequencies[1][char] > frequencies[0][char]:
            return False
    return True