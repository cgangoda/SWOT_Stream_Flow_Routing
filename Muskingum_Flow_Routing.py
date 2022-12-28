# import libraries
from __future__ import division
import numpy as np

# definition variables
I = np.array([93, 137, 208, 320, 442, 546, 630, 678, 691, 675, 634, 571, 477,
              390, 329, 247, 184, 134, 108, 90])
C1 = 0.0631
C2 = 0.3442
C3 = 0.5927

Q = np.empty(20) # defining an enply array
Q[0] = 85 

# apply routing algorithm
for i in range(1,20):
    Q[i] = C1*I[i] + C2*I[i-1] + C3*Q[i-1]

# plotting
import matplotlib.pyplot as plt
plt.plot(I, '-*', label='Inflow')
plt.plot(Q, '--s', label='Outflow')
plt.xlabel('Time', fontsize=20)
plt.ylabel('Flow', fontsize=20)
plt.legend()
plt.savefig('muskingum.png')
