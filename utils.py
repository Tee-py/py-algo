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

