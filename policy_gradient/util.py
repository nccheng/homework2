from gym.spaces import Box, Discrete
import numpy as np
from scipy.signal import lfilter

def flatten_space(space):
	if isinstance(space, Box):
		return np.prod(space.shape)
	elif isinstance(space, Discrete):
		return space.n
	else:
		raise ValueError("Env must be either Box or Discrete.")

"""
Problem 3:

1. Read the example provided in HW2_Policy_Graident.ipynb
2. Uncomment below function and implement it.

Sample solution is about 1~7 lines.
"""

def discount_cumsum(x, discount_rate):
    # YOUR CODE HERE >>>>>>
    # return ???
    dis_cumsum_np = np.zeros(len(x))
    for idx in xrange(len(x)):
         for index, item in enumerate(x[idx:]):
            dis_cumsum_np[idx] += item * discount_rate ** index
    return dis_cumsum_np
    # <<<<<<<<
