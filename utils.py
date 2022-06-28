import time

# closures
def outer(arg):

    def inner():
        print(f'This is the outer Arg --> {arg}')
    return inner

# decorators
def decorator(func):

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        resp = func()
        end = time.perf_counter()
        print(f'{func.__name__} Executed in {end - start} Secs')
        return resp
    return wrapper


def power(x, y):
    print(x,y)
    if (y == 0): return 1
    elif (int(y % 2) == 0):
        return (power(x, int(y / 2)) *
               power(x, int(y / 2)))
    else:
        return (x * power(x, int(y / 2)) *
                   power(x, int(y / 2)))




res = power(2,2)
print(res)
