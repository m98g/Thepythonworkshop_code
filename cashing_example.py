import time 
import functools

@functools.lru_cache(maxsize=2)
def func(x):
    time.sleep(1)
    print(f"Heavy operation of {x}")
    return x * 10

print("Func returned:", func(1))
print("Func returned:", func(2))
print("Func returned:", func(3))
print("Func returned:", func(3))
print("Func returned:", func(2))
print("Func returned:", func(1))


# second way of doing it 
def func(x):
    time.sleep(1)
    print(f"Heavy operation of {x}")
    return x * 10

cached_func = functools.lru_cache()(func)

print("Cached func returned:", cached_func(1))
print("Cached func returned:", cached_func(1))
print("Func returned:", func(1))
print("Func returned:", func(1))