#!/usr/bin/python
import sys

import matplotlib.pyplot as plt
import numpy as np

filename = sys.argv[1]
banks = []
with open(filename, 'r') as f:
	for line in f:
		banks.append([int(i) for i in line.split(',')])

banks = np.array(banks)
print banks.shape

plt.pcolor(banks)
plt.colorbar()
plt.show()
