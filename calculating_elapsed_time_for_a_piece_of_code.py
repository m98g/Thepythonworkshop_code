import time
import random

now = time.time_ns()
print(now)

l = [random.randint(1, 999) for _ in range(10 * 3)]
print(l)

later = time.time_ns()
print(later)

print(later - now)