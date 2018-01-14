#!/usr/bin/python
import sys

import matplotlib.pyplot as plt
import numpy as np

filename = sys.argv[1]
banks = []
with open(filename, 'r') as f:
	for line in f:
		banks.append([int(i) for i in line.split(',')])

icnt_l2 = np.array(banks[::4])
print icnt_l2.shape
icnt_l2_writes = np.array(banks[1::4])

l2_dram = np.array(banks[2::4])
print l2_dram.shape
l2_dram_writes = np.array(banks[3::4])

for i,val in np.ndenumerate(icnt_l2_writes):
  if val == 0:
    icnt_l2[i] = -icnt_l2[i]

for i,val in np.ndenumerate(l2_dram_writes):
  if val == 0:
    l2_dram[i] = -l2_dram[i]

plt.pcolor(icnt_l2)
plt.colorbar()
plt.show()

plt.pcolor(l2_dram)
plt.colorbar()
plt.show()
