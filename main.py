import time


def calculate_time(func):
    def funs(a):
        t = time.time()
        funsc = func(a)
        t2 = time.time()
        return funsc, print(round(t2-t,2))
    return funs

@calculate_time
def some_function(numbers):
    spisok = []
    for i in range(1, numbers + 1):
        str_numbers = str(i)
        spisok.append(i)
some_function(int(input()))
