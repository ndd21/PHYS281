#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# read density.txt and store data into a numpy two-dimensional array
data_file = 'density.txt'
density = np.loadtxt(data_file)

# read data_description.txt and store information in the proper variables
with open('data_description.txt') as file:
   for line in file:
       if "xmin" in line:
           idx = line.index("=")
           xmin = float(line[idx+1:-1])
       elif "xmax" in line:
           idx = line.index("=")
           xmax = float(line[idx+1:-1])
       elif "ymin" in line:
           idx = line.index("=")
           ymin = float(line[idx+1:-1])  
       elif "ymax" in line:
           idx = line.index("=")
           ymax = float(line[idx+1:-1])  
       elif "xlabel" in line:
           idx = line.index("=")
           xlabel = line[idx+1:-1]
       elif "ylabel" in line:
           idx = line.index("=")
           ylabel = line[idx+1:-1]  
       elif "clabel" in line:
           idx = line.index("=")
           clabel = line[idx+1:-1]

# create a pseudocolor plot
fig = plt.figure()

ax = fig.add_subplot(111)

c = ax.imshow(density,cmap='viridis',extent=[xmin, xmax, ymin, ymax], interpolation='antialiased',origin='lower')
ax.set_xlabel(xlabel, fontsize=20)
ax.set_ylabel(ylabel, fontsize=20)
ax.tick_params(labelsize=20)
cbar = fig.colorbar(c)
cbar.set_label(clabel, fontsize=20)
cbar.ax.tick_params(labelsize=20)

fig.tight_layout()

plt.show()

