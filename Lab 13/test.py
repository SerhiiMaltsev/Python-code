import map_reduce

def wiggle(a,b):
    a, b = abs(a), abs(b)
    if a > b:
        a,b = b,a
    c = b % a
    if c == 0:
        return a + b
    return c
def waggle(a):
    if a < 0:
        return -2*a
    else:
        return 2*a+1
x = [3, -1, 4, -1, 5, -9, 2, -6, 5, -3, 5]

print(map_reduce.myreduce(wiggle, x))
print(map_reduce.mymap(waggle, x))
print(map_reduce.myreduce(wiggle, map_reduce.mymap(waggle, x)))
print(x)