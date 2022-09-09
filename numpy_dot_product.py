import numpy as np

x = np.arange(1, 101).reshape(20,5)
y = np.arange(1, 101).reshape(20,5)
# have to read the documentation
z = np.dot(x, y)
print(z)
