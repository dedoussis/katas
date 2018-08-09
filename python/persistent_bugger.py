def persistence(n):
    iter = 0
    while len(str(n)) > 1:
        digits = list(map(int,str(n)))
        n = reduce(lambda x, y: x*y, digits)
        iter += 1
    return iter