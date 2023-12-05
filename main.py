def niker(*args):
    b = []
    for a in args:
        if isinstance(a, int) or isinstance(a, float):
            b.append('.' * a)
    return print(b)


niker(1, 2, 2, 8, 8, 9, 2)

