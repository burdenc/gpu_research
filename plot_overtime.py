#!/usr/bin/python
import sys

import matplotlib.pyplot as plt
import numpy as np

def average_down(arr, factor):
  if factor == 1:
    return arr

  old_shape = str(arr.shape)

  pad_amnt = (((arr.shape[1] // factor) + 1) * factor) - arr.shape[1]
  arr = np.pad(arr, ((0,0), (0,pad_amnt)), 'constant')

  x_shape = arr.shape[0]
  y_steps = arr.shape[1] // factor
  arr = arr.reshape((x_shape, y_steps, factor)).mean(2)

  print "%s -> %s" % (old_shape, str(arr.shape))
  return arr

def remove_non_writes(arr, arr_writes):
  for i,val in np.ndenumerate(arr_writes):
    if val == 0:
      arr[i] = -arr[i]

def graph(queue, queue_writes, average_factor):
  remove_non_writes(queue, queue_writes)
  queue = average_down(queue, average_factor)

  plt.pcolor(queue)
  plt.colorbar()
  plt.show()


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
icnt_l2_writes = np.array(banks[1::4])
graph(icnt_l2, icnt_l2_writes, mean_factor)

del icnt_l2, icnt_l2_writes

l2_dram = np.array(banks[2::4])
l2_dram_writes = np.array(banks[3::4])
graph(l2_dram, l2_dram_writes, mean_factor)
