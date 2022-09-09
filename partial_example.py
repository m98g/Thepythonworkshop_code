import functools

def func(x, y, z):
    print("x", x)
    print("y", y)
    print("z", z)

func(1, 2, 3)
# will allways pass Wops as for z.
new_func = functools.partial(func, z="Wops")
new_func(1,2)

new_func = functools.partial(func, "Wops")
new_func(1,2)