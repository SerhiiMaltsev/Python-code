#Serhii Maltsev sm5zj


def mean(a, b, c):
    return (a + b + c)/3


def median(a, b, c):
    x = []
    if (a >= b) and (a >= c) and (b >= c):
        x = [c, b, a]
    if (a >= b) and (a >= c) and (c >= b):
        x = [b, c, a]
    if (b >= a) and (b >= c) and (a >= c):
        x = [c, a, b]
    if (b >= a) and (b >= c) and (c >= a):
        x = [a, c, b]
    if (c >= a) and (c >= b) and (a >= b):
        x = [b, a, c]
    if (c >= a) and (c >= b) and (b >= a):
        x = [a, b, c]
    return x[1]


def rms(a, b, c):
    return (mean(a*a, b*b, c*c))**0.5


def middle_average(a, b, c):
    x = mean(a, b, c)
    y = median(a, b, c)
    z = rms(a, b, c)
    return median(x, y, z)
