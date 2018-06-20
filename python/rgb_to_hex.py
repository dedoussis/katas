def rgb(r, g, b):
    rgb = list(map(lambda x: max(0, min(x, 255)), [r, g, b]))
    return "{:02X}{:02X}{:02X}".format(*rgb)