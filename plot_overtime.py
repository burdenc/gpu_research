#!/usr/bin/python
import sys

import matplotlib.pyplot as plt
import numpy as np

def average_down(arr, factor):
  pad_amnt = (((arr.shape[1] // factor) + 1) * factor) - arr.shape[1]
  arr = np.pad(arr, ((0,0), (0,pad_amnt)), 'constant')

  x_shape = arr.shape[0]
  y_steps = arr.shape[1] // factor
  arr = arr.reshape((x_shape, y_steps, factor)).max(2)
  return arr

filename = sys.argv[1]
try:
  mean_factor = int(sys.argv[2])
except:
  mean_factor = 1

banks = []
with open(filename, 'r') as f:
	for line in f:
		banks.append([int(i) for i in line.split(',')])

icnt_l2 = np.array(banks[::4])
print icnt_l2.shape
if mean_factor != 1:
  icnt_l2 = average_down(icnt_l2, mean_factor)

print icnt_l2.shape
#icnt_l2_writes = np.array(banks[1::4])

#l2_dram = np.array(banks[2::4])
#print l2_dram.shape
#l2_dram_writes = np.array(banks[3::4])

#for i,val in np.ndenumerate(icnt_l2_writes):
#  if val == 0:
#    icnt_l2[i] = -icnt_l2[i]

#for i,val in np.ndenumerate(l2_dram_writes):
#  if val == 0:
#    l2_dram[i] = -l2_dram[i]

plt.pcolor(icnt_l2)
plt.colorbar()
plt.show()

plt.pcolor(l2_dram)
plt.colorbar()
plt.show()
