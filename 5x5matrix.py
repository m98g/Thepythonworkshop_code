import numpy as np
from numpy import random

# Seeds are used to allways get the same "random" number again. So it is replicatable.
np.random.seed(seed=60)

random_square = np.random.rand(5,5)
print(random_square[0].mean())
print(random_square.mean())
print(random_square[:,4].mean())
